# agregar libreria websocket-client
# version 0.57.0
import json
import logging
import websocket
import ssl
from multiprocessing import Process

import socket
import traceback


def etiqueta(nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades, ancho, largo,  codigo ):
    message = b"^XA" \
             b"^FO30, 40^ADN, 61, 33^FD %s ^FS" \
             b"^FO500, 20^ADN 11, 7^FD # ETIQUETA ^FS" \
             b"^FO555, 40^ADN, 20, 11^FD %s ^FS" \
             b"^FO30, 110^ADN 26, 11^FD CODIGO: ^FS" \
             b"^FO120, 110^ADN, 26, 11^FD %s ^FS" \
             b"^FO30, 150^ADN, 26,11^FD PED: ^FS" \
             b"^FO120, 150^ADN, 26, 11^FD %s ^FS" \
             b"^FO300, 150^ADN, 26, 11^FD OT: ^FS" \
             b"^FO400, 150^ADN, 26, 11^FD %s ^FS" \
             b"^FO30, 190^ADN, 26, 11^FD CANT: ^FS" \
             b"^FO120, 190^ADN, 36, 20^FD %s ^FS" \
             b"^FO300, 190^ADN, 26, 11^FD PESO: ^FS" \
             b"^FO400, 190^ADN, 36, 20^FD %s%s ^FS" \
             b"^FO30, 240^ADN. 26, 11^FD ANCHO: ^FS" \
             b"^FO120, 240^ADN, 36, 20^FD %s ^FS" \
             b"^FO300, 240^ADN. 26, 11^FD LARGO: ^FS" \
             b"^FO400, 240^ADN, 36, 20^FD %s ^FS" \
             b"^FO200, 310^ADN, 36, 20" \
             b"^B5N, 100, Y, N" \
             b"^FD %s^FS" \
             b"^XZ" % (nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades, ancho, largo, codigo)

    return message


def etiqueta_empres_x(diccionario):
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    pot = 9100
    nombre_empresa = diccionario['nombre_empresa']
    codigo = diccionario['testo']
    pedido = diccionario['descripcion']
    ot = diccionario['ot']
    cantidad = diccionario['cantidad']
    peso = diccionario['peso']
    unidades = diccionario['unidades']
    ancho = diccionario['ancho']
    largo = diccionario['largo']
    n_etiqueta = diccionario['n_etiqueta']
    codigo_barras = diccionario['codigo']

    try:
        mysocket.connect((host, pot))
        mysocket.send(
            etiqueta(nombre_empresa, n_etiqueta, codigo, pedido, ot,
                     cantidad, peso, unidades, ancho, largo, codigo_barras))
        mysocket.close()
    except:
        print 'Error de comunicacion: %s' % traceback.format_exc()

    return


def on_mensaje(ws, message):
    try:
        if 'anonymous' in message:
            return

        datos = json.loads(message, object_hook=dict)
        etiqueta_empres_x(datos)
    except:
        raise


def on_error(ws,error):
    print (error)


def on_close(ws):
    print ('ws closed')


def iniciar_con_hilo():
    p = Process(target=iniciar)
    p.start()


def iniciar():
    url='wss://3.239.100.193:9000'
    key = 'desarrollo'
    canal = 'des'
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


iniciar()