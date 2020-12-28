# -*- coding: utf-8 -*-
import socket
import procesamiento
import time
import traceback
import log


"""------------------------------------------------------------------
    CONSTANTES PARA LA CONEXIÒN DE DATOS
------------------------------------------------------------------"""

TCP_IP = '0.0.0.0'
TIMEOUT_CONEXION = 5
TCP_PORT = 46583
BUFFER_SIZE = 1024


def iniciarServidor():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                                               # Establecimiento del socket
    s.bind((TCP_IP, TCP_PORT))                                                                                          # Arranque del socket
    s.settimeout(TIMEOUT_CONEXION)
    s.listen(1)                                                                                                         # Modo esuchar modulo

    while True:
        try:
            #s.settimeout(2)
            sc, addr = s.accept()
            try:
                procesamiento.procesar(sc)
            except:
                log.logging.error("error conexion")
                pass
        except:
            log.logging.error("timeout")
            pass

if __name__ == '__main__':
    log.logging.info("iniciando servidor")
    while True:
        try:
            iniciarServidor()
            time.sleep(1)
            log.logging.info("intentando conectar")
        except:
            log.logging.error("Error: %s" % traceback.format_exc())
            pass
