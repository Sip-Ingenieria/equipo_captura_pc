# -*- coding: utf-8 -*-
import socket
import procesamiento
import config.config as configuracion
import time
import traceback
import log
import modulos.impresora.main as impresora
import modulos.bascula.main as bascula
from multiprocessing import Process
import RunSocket
import win32api, win32event
import os, sys
from winerror import ERROR_ALREADY_EXISTS

import time
import random

"""------------------------------------------------------------------
    CONSTANTES PARA LA CONEXIÒN DE DATOS
------------------------------------------------------------------"""

TIMEOUT_CONEXION = 30
TCP_PORT = 46583


logger = log.configurar('equipo_captura_pc')



def conectar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT_CONEXION)

    try:
        s.connect((configuracion.TCP_IP_CLIENTE, TCP_PORT))
        procesamiento.procesar(s)
    except:
        logger.error("Error: %s" % traceback.format_exc())
        pass

    s.close()


def inciar_cliente():
    logger.info("iniciando cliente")
    while True:
        try:
            conectar()
        except:
            logger.error("Error: %s" % traceback.format_exc())
            pass

        time.sleep(1)


def iniciar_impresora_hilo():
    while True:
        impresora.iniciar()
        time.sleep(1)


def operacion():
    p = None
    q = None
    z = None

    if configuracion.MODULO_BASCULA is True:
        p = Process(target=bascula.iniciar, name='bascula')
        p.start()
    if configuracion.MODULO_CAPTURA is True:
        q = Process(target=inciar_cliente, name='cliente')
        q.start()
    if configuracion.MODULO_IMPRESORA is True:
        z = Process(target=iniciar_impresora_hilo, name='impresora_hilo')
        z.start()
        #while True:
        #    impresora.iniciar()
        #    time.sleep(1)

    if p is not None:
        p.join()
    if q is not None:
        q.join()
    if z is not None:
        z.join()


if __name__ == '__main__':
    

    mutex = win32event.CreateMutex(None, False, 'api')
    error = win32api.GetLastError()
    print(error)

    if error == ERROR_ALREADY_EXISTS:
        logger.info("esta app ya esta abierta")
        sys.exit('esta app ya esta abierta')
        #exit('esta app ya esta abierta')

    tiempoRandom = random.randint(2, 10)

    time.sleep(tiempoRandom)

    if RunSocket.consultar() is True:
        exit()
    p = RunSocket.iniciar_hilo()
    operacion()
    if p is not None:
        p.join()
