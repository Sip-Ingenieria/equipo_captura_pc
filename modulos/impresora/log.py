import logging
import logging.config
from logging.handlers import RotatingFileHandler

ruta_log = 'C:\equipo_captura_pc\logs\servicio_mpresora.log'

#logging.config.fileConfig()
logger = logging.getLogger('servicio_mpresora')
#handlers = RotatingFileHandler(filename=ruta_log, maxBytes=100000, backupCount=10)
#formato = logging.Formatter('%(asctime)s %(message)s')
#handlers.setFormatter(formato)
#logger.setLevel(logging.DEBUG)
#logger.addHandler(handlers)

#logging.basicConfig(
#    filename='\equipo_captura_pc\logs\servicio_mpresora.log',
#    level=logging.DEBUG,
#    filemode='w',
#    format='%(asctime)s %(message)s'
#)

#filename='C:\equipo_captura_pc\logs\servicio_mpresora.log'