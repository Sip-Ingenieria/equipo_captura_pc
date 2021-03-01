import socket
from multiprocessing import Process
import config.config as configuracion
import log


def consultar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((configuracion.DIRECCION_IP_BLOQUEO, configuracion.PUERTO_SOCKET_BLOQUEO))
    if result == 0:
       return True
    else:
       return False


def abrir_puerto():

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((configuracion.DIRECCION_IP_BLOQUEO, configuracion.PUERTO_SOCKET_BLOQUEO))
            s.settimeout(configuracion.TIMEOUT_CONEXION_BLOQUEO)
            s.listen(1)
            sc, addr = s.accept()

        except:
            log.logging.error("timeout")
            pass


def iniciar_hilo():
    p = Process(target=iniciar)
    p.start()
    return p


def iniciar():
    abierto = consultar()
    if abierto is True:
        exit()
    else:
        abrir_puerto()
