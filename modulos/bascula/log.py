import logging
from logging.handlers import RotatingFileHandler


ruta_log = 'servicio_bascula.log'
logger = logging.getLogger('servicio_bascula')
handlers = RotatingFileHandler(filename=ruta_log, maxBytes=100000, backupCount=10)
formato = logging.Formatter('%(asctime)s %(message)s')
handlers.setFormatter(formato)
logger.setLevel(logging.DEBUG)
logger.addHandler(handlers)

#logging.basicConfig(
#    filename='\equipo_captura_pc\logs\servicio_bascula.log',
#    level=logging.DEBUG,
#    filemode='w',
#    format='%(asctime)s %(message)s'
#)


