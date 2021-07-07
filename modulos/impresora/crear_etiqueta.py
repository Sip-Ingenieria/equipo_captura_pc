from Etiqueta import Etiqueta
import json
#import logging
import websocket
import ssl
from multiprocessing import Process

import sys
sys.path.append( '../../' )
import log

def etiqueta_empres_x(diccionario):
    nombre=diccionario['nombre_etiqueta']
    empresa=diccionario['nombre_empresa']
    ancho1=179
    ancho2=89
    alto1=45
    alto2=90
    alto3=135
    alto4=179

    tamano_tablero_ancho = 180*6
    tamano_tablero_alto = 180*3
    parteA = [0,0,ancho1*6,alto1*3]
    parteB = [0,alto1*3,ancho1*6,alto2*3]
    partec = [0,alto2*3,ancho2*6,alto3*3]
    parteD = [ancho2*6,alto2*3,ancho1*6,alto3*3]
    parteE = [0,alto3*3,ancho1*6,alto4*3]

    etiqueta_bosquejo = Etiqueta(nombre=nombre, empresa=empresa, parteA=parteA, parteB=parteB, parteC=partec,
                                 parteD=parteD, parteE=parteE)

    estructura_etiqueta = etiqueta_bosquejo.estructura_etiqueta(tamano_tablero_ancho, tamano_tablero_alto)


    directorio_fuete='C:\Windows\Fonts'
    fuente='Arial.ttf'
    tamano_letra = 30


    ## PARTE A ##
    coordenada = (5, 45)
    align = 'center'
    texto = diccionario['nombre_empresa']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto,coordenada,tamano_letra,directorio_fuete,fuente,align,estructura_etiqueta)

    coordenada = (358, 0)
    align = 'left'
    texto = ' PRODUCCION ' + diccionario['produccion']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (358, 90)
    align = 'left'
    texto = ' LOGISTICA ' + diccionario['logistica']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (716, 0)
    align = 'left'
    texto = 'Nro Etiqueta'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (716, 45)
    align = 'left'
    texto = '%s' % diccionario['numero_etiqueta']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    ## PARTE B ###
    coordenada = (5, 135)
    align = 'left'
    texto = 'cod: %s' %diccionario['codigo']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (5, 225)
    align = 'left'
    texto = 'EXR 100 HR v7 C3/16 1x.25'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (358, 135)
    align = 'left'
    texto = 'pedido: %s' % diccionario['numero_pedido']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (716, 135)
    align = 'left'
    texto = 'OT: %s' % diccionario['ot']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    ## PARTE C ###

    coordenada = (5, 270)
    align = 'left'
    texto = 'TRAMOS'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 270)
    align = 'left'
    texto = '%s' % diccionario['tramos']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (5,315)
    align = 'left'
    texto = 'ANCHO(m)'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 315)
    align = 'left'
    texto = '%s' % diccionario['ancho']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (5, 360)
    align = 'left'
    texto = 'PESO/m2'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 360)
    align = 'left'
    texto = '%s' % diccionario['peso']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    ## PARTE D ###

    coordenada = (534, 270)
    align = 'left'
    texto = 'M2'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (804, 270)
    align = 'left'
    texto = '%s' % diccionario['m2']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (534, 315)
    align = 'left'
    texto = 'LARGO'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (804, 315)
    align = 'left'
    texto = '%s' % diccionario['largo']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (534, 360)
    align = 'left'
    texto = 'TOTAL (Kg)'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (804, 360)
    align = 'left'
    texto = '%s' % diccionario['total']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    ##  PARTE E ##
    coordenada = (5, 405)
    align = 'left'
    texto = 'MQ:'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 405)
    align = 'left'
    texto = '%s' % diccionario['mq']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (534, 405)
    align = 'left'
    texto = '%s' % diccionario['fecha']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (804, 405)
    align = 'left'
    texto = '%s' % diccionario['hora']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (5, 450)
    align = 'left'
    texto = 'OPE:'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 450)
    align = 'left'
    texto = '%s' % diccionario['nombre_operario']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    coordenada = (5, 495)
    align = 'left'
    texto = 'OBS:'
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)
    coordenada = (267, 495)
    align = 'left'
    texto = '%s' % diccionario['OBS']
    etiqueta = etiqueta_bosquejo.agregar_texto_etiqueta(texto, coordenada, tamano_letra, directorio_fuete, fuente, align,
                                                        estructura_etiqueta)

    etiqueta_bosquejo.imprimir(etiqueta)

    return


def on_mensaje(ws,message):
    try:
        if 'anonymous' in message:
            return

        datos = json.loads(message, object_hook=dict)
        etiqueta_empres_x(datos)

    except:
        raise


def on_error(ws,error):
    print (error)
    log.logging.error("crear_etiquetas error %s" % error)


def on_close(ws):
    print  ('crear_etiquetas : ws closed')
    log.logging.info("crear_etiquetas : ws closed")


def iniciar_con_hilo():
    p = Process(target=iniciar)
    p.start()


def iniciar():
    url='wss://54.94.54.73:8888'
    key = 'desarrollo'
    canal='des'
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

# diccionario = dict(
#     nombre_etiqueta='etiqueta prueba',
#     nombre_empresa='ICOMALLAS...',
#     produccion='x',
#     logistica='',
#     numero_etiqueta='1000',
#     codigo='123456',
#     numero_pedido='505050',
#     ot=16490,
#     tramos=20000,
#     ancho =1000,
#     peso = 0.444,
#     m2=50000,
#     largo=2500,
#     total=22200,
#     mq='MDL',
#     fecha='27.08.2020',
#     hora='21:08:59',
#     nombre_operario='NOMBRE OPERARIO COMPLETO',
#     OBS=''
# )

#etiqueta_empres_x(diccionario=diccionario)
