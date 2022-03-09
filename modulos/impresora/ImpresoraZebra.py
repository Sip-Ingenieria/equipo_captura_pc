import socket
import traceback
import win32print, win32ui, win32con
import sys
sys.path.append( '../../' )
import log

logger = log.configurar('servicio_impresora')

class ImpresoraZebra:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def etiqueta(self, nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades,
                 ancho, unidades_ancho, largo, unidades_largo, codigo, nombre_producto, codigo_b='barras'):

        if codigo_b == 'barras':
            codigo_barras = "^B2N, 100, Y, N, N" \
            "^FD %s^FS" % codigo

        else:
            codigo_barras = "^BQN, 2, 2" \
                            "^FDHM,A ETIQ: {n_etiqueta} " \
                            "REF: {referencia} " \
                            "LARG: {largo} " \
                            "ANCH: {ancho} " \
                            "PESO: {peso} " \
                            "CANT: {cantidad} " \
                            "PED: {op} " \
                            "^FS".format(referencia=testo, largo=largo, ancho=ancho,
                                         peso=peso, cantidad=cantidad, op=descripcion, n_etiqueta=n_etiqueta)

        message = "^XA" \
                  "^LH 129,10" \
                  "^FO0, 010^ADN, 26, 11^FD REF : ^FS" \
                  "^FO65, 10 ^ADN, 26, 11^FD {referencia}^FS" \
                  "^FO0, 40^ADN, 26, 11^FD LARG: ^FS" \
                  "^FO65, 40^ADN, 26, 11^FD{largo}^FS" \
                  "^FO0, 70^ADN, 26, 11^FD ANCH: ^FS" \
                  "^FO65, 70^ADN, 26, 11^FD{ancho}^FS" \
                  "^FO0, 100^ADN, 26, 11^FD PESO: ^FS" \
                  "^FO65, 100^ADN, 26, 11^FD{peso}^FS" \
                  "^FO0, 130^ADN, 26, 11^FD CANT: ^FS" \
                  "^FO65, 130^ADN, 26, 11^FD{cantidad}^FS" \
                  "^FO0, 160^ADN, 26, 11^FD PED : ^FS" \
                  "^FO65, 160^ADN, 26, 11^FD {op}^FS" \
                  "^FO50, 173^ADN, 36, 20" \
                  "{codigo_qr_bar}" \
                  "^LH40,10" \
                  "^FWB" \
                  "^FO60,040^AD,26,11^FD #ETIQUETA: {n_etiqueta}^FS" \
                  "^FO0,10^AD,26,11^FB250,2,0,C^FD{nombre_producto}^FS" \
                  "^FWR" \
                  "^FO470,40^AD,26,11^FD #ETIQUETA: {n_etiqueta}^FS" \
                  "^FO510,25^AD,26,11^FB250,2,0,C^FD{nombre_producto}^FS" \
                  "^LH5,10" \
                  "^FWB" \
                  "^FO0,0^AD,26,11^FD OT: {orden_trabajo}^FS" \
                  "^FWR" \
                  "^FO610,180^AD,26,11^FD OT: {orden_trabajo}^FS" \
                  "^LH 129,10" \
                  "^FWN" \
                  "^FO200, 010^ADN, 26, 11^FD REF : ^FS" \
                  "^FO265, 10 ^ADN, 26, 11^FD {referencia}^FS" \
                  "^FO200, 40^ADN, 26, 11^FD LARG: ^FS" \
                  "^FO265, 40^ADN, 26, 11^FD{largo}^FS" \
                  "^FO200, 70^ADN, 26, 11^FD ANCH: ^FS" \
                  "^FO265, 70^ADN, 26, 11^FD{ancho}^FS" \
                  "^FO200, 100^ADN, 26, 11^FD PESO: ^FS" \
                  "^FO265, 100^ADN, 26, 11^FD{peso}^FS" \
                  "^FO200, 130^ADN, 26, 11^FD CANT: ^FS" \
                  "^FO265, 130^ADN, 26, 11^FD{cantidad}^FS" \
                  "^FO200, 160^ADN, 26, 11^FD PED : ^FS" \
                  "^FO265, 160^ADN, 26, 11^FD {op}^FS" \
                  "^FO250, 173^ADN, 36, 20" \
                  "{codigo_qr_bar}" \
                  "^XZ".format(referencia=testo, largo=largo, ancho=ancho, peso=peso, cantidad=cantidad,
                               op=descripcion,codigo_qr_bar=codigo_barras, n_etiqueta=n_etiqueta,
                               nombre_producto=nombre_producto, orden_trabajo=ot)

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
        unidades_ancho = 'MTS'
        unidades_largo = 'MTS'
        unidades_cantidad = 'UND'

        # fromatear valores
        # valores del peso
        peso_str = self.formato(peso, unidades, und_peso=True)
        # valores metros
        largo_str = self.formato(float(largo[:-2]), unidades_largo)
        ancho_str = self.formato(float(ancho[:-2]), unidades_ancho)
        # valores de cantidad
        cantidad_str = self.formato(float(cantidad), unidades_cantidad)

        etiqueta = self.etiqueta(nombre_empresa, n_etiqueta, codigo, pedido, ot,
                                 cantidad_str, peso_str, unidades, ancho_str, unidades_ancho, largo_str, unidades_largo,
                                 codigo_barras, nombre_producto, codigo_b='QR')
        return etiqueta

    def formato(self, valor, unidades, und_peso=False):

        # valores fijos
        max_leng = 10
        max_und_str = 3
        espacio_vacio = ' '

        # transformar valor en str con un espacio y 2,1,0 puntos flotantes
        if (valor > 0) & (valor <= 99):
            print(1)
            n_strin = ' {:,.2f}'.format(valor)
        elif (valor > 100) & (valor <= 999):
            print(2)
            n_strin = ' {:,.1f}'.format(valor)
        else:
            print(3)
            n_strin = ' {:.0f}'.format(valor)

        print (n_strin)

        if und_peso is True:
            if unidades.upper() == 'KILOS':
                unidades = 'KG'
            elif unidades.upper() == 'GRAMOS':
                unidades = 'G'
            else:
                unidades = 'TON'

        # mirar cuantos espacios agregar
        multi = max_leng - len(n_strin) - max_und_str
        # contruir valor con uniades
        valor_frm = n_strin + (espacio_vacio * multi) + unidades
        len(valor_frm)

        return valor_frm

    def imprimir_ethernet(self, etiqueta):
        mysocket = self.mysocket

        try:
            mysocket.connect((self.ip, self.port))
            mysocket.send(etiqueta)
            mysocket.close()
        except:
            #print traceback.format_exc()
            logger.info('Error de comunicacion: %s' % traceback.format_exc())

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
                logger.info('error imprimiendo: %s' % traceback.format_exc())

            finally:
                win32print.EndDocPrinter(hPrinter)
        except:
            logger.info('error abriendo el documento para imprimir: %s' % traceback.format_exc())

        finally:
            win32print.ClosePrinter(hPrinter)



