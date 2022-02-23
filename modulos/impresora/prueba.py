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
diccionario['testo'] = '27067.'
diccionario['descripcion'] = 'pp 070'
diccionario['ot'] = '156-789'
referencia = 'E x R xxxxxxxx'
diccionario['cantidad'] = 5000
diccionario['peso'] = 78
diccionario['ancho'] = '1.39 M'
diccionario['largo'] = '1.39 M'
diccionario['n_etiqueta'] = 150456
diccionario['n_producto'] = ''
diccionario['unidades'] = 'kilos'
diccionario['codigo'] = 1234567890
diccionario['tipo_codigo'] = 'QR'

impresoraZebra = ImpresoraZebra(host, pot)

etiqueta = impresoraZebra.crear_etiqueta(diccionario, archivoConfig.NOMBRE_EMPRESA)
impresoraZebra.imprimir_ethernet(etiqueta)