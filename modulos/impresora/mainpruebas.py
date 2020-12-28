# coding=utf-8
import main as mainCliente
import log
import time
import traceback
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log.logging.info('iniciando cliente')
    while True:
        try:
            mainCliente.iniciar()
            log.logging.info('intentando conectar')
        except:
            log.logging.info('Error: %s' % traceback.format_exc())
            pass
        time.sleep(1)



