# agregar libreria websocket-client
# version 0.57.0
import json
import websocket
import ssl
import traceback
#import modulos.impresora.log as log
import config.config as archivoConfig

import sys
sys.path.append( '../../' )
import log

from multiprocessing import Process
from modulos.impresora.ImpresoraZebra import ImpresoraZebra

logger = log.configurar('servicio_impresora')


def on_mensaje(ws, message):

    impresoraZebra = ImpresoraZebra(archivoConfig.IP, archivoConfig.PORT)
    #print(message)
    try:
        if 'anonymous' in message:
            return

        datos = json.loads(message, object_hook=dict)
        if datos['usuario_id'] == str(archivoConfig.IMPRESORA_ID):
            etiqueta=datos['mensaje_imprimir'].encode('utf8') #un mensaje codificado en utf8
            #etiqueta = impresoraZebra.crear_etiqueta(datos, archivoConfig.NOMBRE_EMPRESA)
            if archivoConfig.TIPO_COMUNICACION == 'USB':
                impresoraZebra.imprimir_usb(etiqueta, archivoConfig.NOMBRE_IMPRESORA)
            else:
                impresoraZebra.imprimir_ethernet(etiqueta)
    except:
        logger.info('error procesando datos: %s' % traceback.format_exc())
        raise


def on_error(ws, error):
    logger.info(' impresora error %s' % error)
    return


def on_close(ws, close_status_code, close_msg):

    # Because on_close was triggered, we know the opcode = 8
    print ('impresora : ws closed')
    logger.info('impresora : ws closed')
    print("on_close args:")

    if close_status_code or close_msg:

        print("close status code: " + str(close_status_code))

        print("close message: " + str(close_msg))

def iniciar_con_hilo():
    p = Process(target=iniciar)
    p.start()
    p.join()


def iniciar():
    #print("impresora....")

    logger.info("iniciando sistema de impresora")

    url = archivoConfig.URL
    key = archivoConfig.KEY
    canal = archivoConfig.CANAL

    websocket.enableTrace(True)
    url_websocket_impresiones_ingresos_insumos = '%s/realtime/%s_impresiones_ingresos_insumos' % (
        url,
        canal
    )
    ws = websocket.WebSocketApp(
        url_websocket_impresiones_ingresos_insumos,
        on_message=on_mensaje,
        on_error=on_error,
        on_close=on_close
    )

    ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})

    return
