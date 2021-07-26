# -*- coding: utf-8 -*-
#import modulos.bascula.log as log


import sys
sys.path.append('../../')
import log

import serial
import serial.tools.list_ports
import time
import traceback
import config.config as configuraciones
import procesamiento

"""------------------------------------------------------------------
    CONSTANTES PARA LA CONEXIÒN DE DATOS
------------------------------------------------------------------"""

TIMEOUT_CONEXION = 1
logger = log.configurar('servicio_bascula')


def pesar():
    linea = ""
    a = 1   # a = 0 #0 en condiciones normales
    p = list(serial.tools.list_ports.comports())   # lista todos los puertos
    for numero in p:
        #print (numero)
        #if numero.device!='/dev/ttyUSB0':
        com = serial.Serial(numero.device, baudrate=configuraciones.VEL_BAUDIOS, timeout=TIMEOUT_CONEXION) #se conecta al primero
        if len(p) == 1:
            break
        linea=com.read()
        if len(linea) == 0:
            com.close()
        else:
            a=1
            break
    #se queda conectado al primero que envie info
    while a:
        linea=""
        try:
            linea = hex(ord(com.read()))
        except serial.SerialException: #intenta volver a conectarse a un puerto libre
            for numero in p:
                #print (numero)
                com = serial.Serial(numero.device, baudrate=configuraciones.VEL_BAUDIOS, timeout=TIMEOUT_CONEXION) #se conecta al primero
                linea=com.read()
                if len(linea) == 0:
                    com.close()
                else:
                    break
        else:
            if linea == '0xff':
                linea= ""
                arreglo = [0,0,0]
                arreglo[0]=hex(ord(com.read()))
                arreglo[1]=hex(ord(com.read()))
                arreglo[2]=hex(ord(com.read()))
                subarreglo1=arreglo[1]
                subarreglo1=subarreglo1[2:]
                subarreglo2=arreglo[2]
                subarreglo2=subarreglo2[2:]
                if arreglo[0] =='0x42':
                    numerodecod = float(subarreglo2)*10+float(subarreglo1)/10
                    # procesamiento.set_valor_bascula(numerodecod)
                    archivo = open(configuraciones.ROUTE, "w")
                    archivo.write("\"" + str(numerodecod)+"\"\r\n")
                    archivo.close()
                    #print(numerodecod)
                    a=1 #a = 0 #0 en condiciones normales


def iniciar():
    logger.info("iniciando sistema de pesaje")

    while True:
        try:
            pesar()
            time.sleep(1)
            logger.info("init")
        except:
            error = "Error: %s" % traceback.format_exc()
            if 'PermissionError' in error:
                pass
            else:
                logger.error("%s" % error)


if __name__ == '__main__':
    iniciar()

