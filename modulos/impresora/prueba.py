from modulos.impresora.ImpresoraZebra import ImpresoraZebra
import json
import websocket
import ssl
import traceback
#import modulos.impresora.log as log
import config.config as archivoConfig
#import main as mn



diccionario = dict()

host = "127.0.0.1"
pot = 9100
n_empresa = 'ICOMALLAS'
diccionario['testo'] = 123456789
diccionario['descripcion'] = 'PF004600'
diccionario['ot'] = '156-789'
referencia = 'E x R xxxxxxxx'
diccionario['cantidad'] = 500
diccionario['peso'] = 78
diccionario['ancho'] = 1.25
diccionario['largo'] = 1.25
diccionario['n_etiqueta'] = 150
diccionario['n_producto'] = ''
diccionario['unidades'] = 'kilos'
diccionario['codigo'] = 1234567890

#impresoraZebra = ImpresoraZebra(host, pot)

#etiqueta = impresoraZebra.crear_etiqueta(diccionario, archivoConfig.NOMBRE_EMPRESA)
#impresoraZebra.imprimir_ethernet(etiqueta)

def on_mensaje(ws, message):
    datos = json.loads(message, object_hook=dict)
    print datos

    #impresoraZebra = ImpresoraZebra(archivoConfig.IP, archivoConfig.PORT)

    #try:
    #    if 'anonymous' in message:
    #        return

    #    datos = json.loads(message, object_hook=dict)
    #    if datos['usuario_id'] == archivoConfig.IMPRESORA_ID:
    #        etiqueta = impresoraZebra.crear_etiqueta(datos, archivoConfig.NOMBRE_EMPRESA)
    #        if archivoConfig.TIPO_COMUNICACION == 'USB':
    #            impresoraZebra.imprimir_usb(etiqueta, archivoConfig.NOMBRE_IMPRESORA)
    #        else:
    #            impresoraZebra.imprimir_ethernet(etiqueta)
    #except:
    #    print 'error procesando datos: %s' % traceback.format_exc()
    #    #logger.info('error procesando datos: %s' % traceback.format_exc())
    #    raise

url = archivoConfig.URL
key = archivoConfig.KEY
canal = archivoConfig.CANAL
print url,key,canal
websocket.enableTrace(True)
url_websocket_impresiones_ingresos_insumos = '%s/realtime/%s_impresiones_ingresos_insumos' % (
    url,
    canal
)
print url_websocket_impresiones_ingresos_insumos
ws = websocket.WebSocketApp(
    url_websocket_impresiones_ingresos_insumos,
    on_message=on_mensaje
)

ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})