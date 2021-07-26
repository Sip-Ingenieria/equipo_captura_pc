import socket
from multiprocessing import Process
import config.config as configuracion
import log
logger = log.configurar('equipo_captura_pc')


def consultar():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((configuracion.DIRECCION_IP_BLOQUEO, configuracion.PUERTO_SOCKET_BLOQUEO))
    logger.error('el codigo que retorna la conexion es: %s' % result)
    print('el codigo que retorna la conexion es: %s' % result)
    if result == 0:
        return True
    elif result == 10061:
        return False
    else:
        return True


def abrir_puerto():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((configuracion.DIRECCION_IP_BLOQUEO, configuracion.PUERTO_SOCKET_BLOQUEO))
            s.listen(1)
            sc, addr = s.accept()
            s.close()
        except:
            logger.error("timeout")
            pass


def iniciar_hilo():
    p = Process(target=iniciar)
    p.start()
    return p


def iniciar():
    logger.error("iniciar run socket")
    abierto = consultar()
    if abierto is True:
        exit()
    else:
        abrir_puerto()
