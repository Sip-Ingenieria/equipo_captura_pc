import socket
import traceback
import log
import win32print, win32ui, win32con


class ImpresoraZebra:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def etiqueta(self, nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades,
                 ancho, unidades_ancho, largo, unidades_largo, codigo, nombre_producto):
        message = "^XA" \
                  "^FO5, 20^ADN, 36, 20^FD %s ^FS" \
                  "^FO500, 20^ADN 26, 11^FD # ETIQUETA ^FS" \
                  "^FO500, 40^ADN, 28, 15^FD %s ^FS" \
                  "^FO30, 90^ADN 26, 11^FD CODIGO: ^FS" \
                  "^FO120, 90^ADN, 26, 11^FD %s ^FS" \
                  "^FO30, 130^ADN, 26, 11^FD %s ^FS" \
                  "^FO30, 170^ADN, 26,11^FD PED: ^FS" \
                  "^FO120, 170^ADN, 26, 11^FD %s ^FS" \
                  "^FO300, 170^ADN, 26, 11^FD OT: ^FS" \
                  "^FO380, 170^ADN, 26, 11^FD %s ^FS" \
                  "^FO30, 210^ADN, 26, 11^FD CANT: ^FS" \
                  "^FO120, 210^ADN, 36, 20^FD %s ^FS" \
                  "^FO300, 210^ADN, 26, 11^FD PESO: ^FS" \
                  "^FO380, 210^ADN, 36, 20^FD %s %s ^FS" \
                  "^FO30, 270^ADN. 26, 11^FD ANCHO: ^FS" \
                  "^FO120, 270^ADN, 36, 20^FD %s ^FS" \
                  "^FO30, 330^ADN. 26, 11^FD LARGO: ^FS" \
                  "^FO120, 330^ADN, 36, 20^FD %s ^FS" \
                  "^FO410, 270^ADN, 36, 20" \
                  "^B5N, 100, Y, N" \
                  "^FD %s^FS" \
                  "^XZ" % (nombre_empresa,
                           n_etiqueta, testo, nombre_producto, descripcion,
                           ot, cantidad, peso, unidades[0], ancho, largo, codigo)

        message_byte = message.encode('utf-8')

        return message_byte

    def crear_etiqueta(self, diccionario, n_empresa):
        nombre_empresa = n_empresa
        codigo = diccionario['testo']
        pedido = diccionario['descripcion']
        ot = diccionario['ot'] if diccionario['ot'] is not None else ""
        cantidad = diccionario['cantidad']
        peso = diccionario['peso']
        unidades = diccionario['unidades']
        ancho = diccionario['ancho']
        largo = diccionario['largo']
        n_etiqueta = diccionario['n_etiqueta']
        codigo_barras = diccionario['codigo']
        nombre_producto = diccionario['n_producto']
        unidades_ancho = 'm'
        unidades_largo = 'm'

        etiqueta = self.etiqueta(nombre_empresa, n_etiqueta, codigo, pedido, ot,
                                 cantidad, peso, unidades, ancho, unidades_ancho, largo, unidades_largo,
                                 codigo_barras,nombre_producto)
        return etiqueta

    def imprimir_ethernet(self, etiqueta):
        mysocket = self.mysocket

        try:
            mysocket.connect((self.ip, self.port))
            mysocket.send(etiqueta)
            mysocket.close()
        except:
            log.logging.info('Error de comunicacion: %s' % traceback.format_exc())

        return

    def imprimir_usb(self, etiqueta, nombre_impresora):
        comando = str(etiqueta).encode('cp437')

        if nombre_impresora is None:
            hPrinter = win32print.OpenPrinter(win32print.GetDefaultPrinter())
        else:
            hPrinter = win32print.OpenPrinter(nombre_impresora)

        try:
            hJob = win32print.StartDocPrinter(hPrinter, 1, ('label', None, 'RAW'))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, comando)
                win32print.EndPagePrinter(hPrinter)
            except:
                log.logging.info('error imprimiendo: %s' % traceback.format_exc())

            finally:
                win32print.EndDocPrinter(hPrinter)
        except:
            log.logging.info('error abriendo el documento para imprimir: %s' % traceback.format_exc())

        finally:
            win32print.ClosePrinter(hPrinter)



