import logging
from logging.handlers import RotatingFileHandler
### cinfiguracion log

def configurar(log_name):
    ruta_log = 'logs\%s.log' % log_name
    logger_proceso = logging.getLogger(log_name)
    handlers = RotatingFileHandler(filename=ruta_log, maxBytes=100000, backupCount=10)
    formato = logging.Formatter('%(asctime)s %(message)s')
    handlers.setFormatter(formato)
    logger_proceso.setLevel(logging.DEBUG)
    logger_proceso.addHandler(handlers)
    return logger_proceso


#handlers = RotatingFileHandler(filename='logs\equipo_captura_pc.log', maxBytes=100000, backupCount=10)
#formato = logging.Formatter('%(asctime)s %(message)s')
#handlers.setFormatter(formato)
#logging.root.addHandler(handlers)
#logging.root.setLevel(logging.DEBUG)
#logging.basicConfig(
#    filename='logs\equipo_captura_pc.log',
#    level=logging.DEBUG,
#    filemode='a',
#    format='%(asctime)s %(message)s',
#)

#ruta_log = 'logs\equipo_captura_pc.log'
#logger = logging.getLogger('equipo_captura_pc')
#handlers = RotatingFileHandler(filename=ruta_log, maxBytes=100000, backupCount=10)
#formato = logging.Formatter('%(asctime)s %(message)s')
#handlers.setFormatter(formato)
#logger.setLevel(logging.DEBUG)
#logger.addHandler(handlers)


