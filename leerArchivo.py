
import config.config as configuracion
import traceback
import log


def leer_archivo():
    try:
        #'C:\\icomallas\registros.txt'
        file=open(configuracion.RUTA_ARCHIVO,"r")        
        content=file.read()
        file.close()
        return content
        #log.logging.error("PESO: %s" % content)
    
    except:
        log.logging.error("Error: %s" % traceback.format_exc())
        return "0"
