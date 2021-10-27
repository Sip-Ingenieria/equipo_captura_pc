# -*- coding: utf-8 -*-
import leerArchivo
import json
from datetime import datetime
import config.config as configuracion
import log

valor_bascula = 0


def set_valor_bascula(valor):
    global valor_bascula
    valor_bascula = valor

"""------------------------------------------------------------------
    CONSTANTES PARA LA CONEXIÒN DE DATOS
------------------------------------------------------------------"""

BUFFER_SIZE = 1024


def convertir_a_formato_salida(data):
   try:
      data = bytes(data, 'utf8')
   except:
      data = bytes(data)
   return data


def formatear_dato(dato):
    nuevo = ''
    indice = 0
    print ('dato = %s' % dato)
    if '-' in dato:
        return '0.0'
    nuevo=dato.replace('"','')
##    for i in dato:
##        if i == '"':
##            indice += 1
##            continue
##        elif (indice == 1) & (i == '0'):
##            indice += 1
##            continue        
##        else:
##            nuevo+= i
##            indice += 1        
##            
    #print ('nuevo = %s' % nuevo)
    return nuevo


def procesar(s):
    val = 0
    while True:
        data = s.recv(BUFFER_SIZE)
        data="".join(map(chr,data))
        # log.logging.info(type(data))
        # log.logging.info("".join(map(chr,data)))
        # log.logging.info("".join(map(chr,bytes(data))))
        if data == '*#':
            # enviar direccion mac
            s.send(convertir_a_formato_salida('{"TT": 6, "mac": "%s"}' % configuracion.MAC))
            # s.send('{"TT": 6, "mac": "%s"}' % configuracion.MAC)
            continue

        if data == '':
            return

        if len(data) == 0:
            return

        #print("data: %s" % data)
        #log.logging.error("INPUT DATA: %s" % data)
        #data_str = "".join(map(chr, data))
        #datajson = json.loads("".join(map(chr,data)))
        
        datajson = json.loads(data)
        if datajson["TT"] == 14 and val == 0:
            dt = datetime.now()            
            # fh = dt.strftime("%S")
            fh = dt.timestamp()
            file = leerArchivo.leer_archivo()
            # pstring = file.strip('"')  # remover los numerales del string
            # pstring = pstring.replace('"', '')
            pstring = formatear_dato(file)
            # pstring = valor_bascula
            # log.logging.error("pstring: %s" % pstring)
            trama = '{"TT": 8,"fh":' + str(fh) + ',"hm": 0,"vp":' + str(pstring) + '}'
            # log.logging.error("OUTPUT: %s" % trama)
            arr = bytes(trama, 'utf8')
            s.send(arr)
            val = 1
        else:
            trama_aux = '{"TT": 6}'
            arr = bytes(trama_aux, 'utf8')
            s.send(arr)
            val = 0

        # log.logging.error("OUTPUT: %s" % arr)
