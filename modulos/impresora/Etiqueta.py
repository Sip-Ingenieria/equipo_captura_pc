from PIL import ImageDraw,Image,ImageWin,ImageFont
import win32ui
import win32print

class Etiqueta:
    pass
    def __init__(self,nombre,empresa,parteA,parteB,parteC,parteD,parteE):
        self.nombre = nombre
        self.empres = empresa
        self.parteA = parteA
        self.parteB = parteB
        self.parteC = parteC
        self.parteD = parteD
        self.parteE = parteE

    def estructura_etiqueta(self,tamano_tablero_ancho,tamano_tablero_alto):

        etiqueta = Image.new('L', ((tamano_tablero_ancho), (tamano_tablero_alto)), color=(0))
        forma_etiqueta = ImageDraw.Draw(etiqueta)
        forma_etiqueta.rectangle(self.parteA, fill='white', outline='black', width=1)
        forma_etiqueta.rectangle(self.parteB, fill='white', outline='black', width=1)
        forma_etiqueta.rectangle(self.parteC, fill='white', outline='black', width=1)
        forma_etiqueta.rectangle(self.parteD, fill='white', outline='black', width=1)
        forma_etiqueta.rectangle(self.parteE, fill='white', outline='black', width=1)

        return etiqueta

    def agregar_texto_etiqueta(self,texto,coordenada,tamano_letra,directorio_fuente,fuente,align,estructura_etiqueta):

        etiqueta = estructura_etiqueta
        etiqueta_texto = ImageDraw.Draw(etiqueta)
        #fnt = ImageFont.load_default()

        fnt = ImageFont.truetype('%s\%s' % (directorio_fuente, fuente), tamano_letra)

        etiqueta_texto.text(coordenada, texto, fill='black', font=fnt,align=align)

        return etiqueta


    ###MODIFICAR PARA QUE SEA MAS GENERAL
    def imprimir(self,etiqueta):
        HORZRES = 8
        VERTRES = 10

        LOGPIXELSX = 88
        LOGPIXELSY = 90

        ANCHO_FISICO = 110
        ALTO_FISICO = 111

        OFSET_FISICO_X = 112
        OFSET_FISICO_Y = 112

        printer_name = win32print.GetDefaultPrinter()

        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        printer_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)

        printer_zise = hDC.GetDeviceCaps(ANCHO_FISICO), hDC.GetDeviceCaps(ALTO_FISICO)

        printer_margin = hDC.GetDeviceCaps(OFSET_FISICO_X), hDC.GetDeviceCaps(OFSET_FISICO_Y)

        # aqui se agrega la etiqueta
        bmp = etiqueta
        # resolucion de la imagen,rotar para que encaje
        # if bmp.size[0] > bmp.size[1]:
        #
        #     bmp = bmp.rotate(90)
        # normalizar segun la resolucion de la imagen
        ratios = [1.0 * printer_area[0] / bmp.size[0], 1.0 * printer_area[1] / bmp.size[1]]

        scala = min(ratios)

        hDC.StartDoc('3')
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        scale_ancho, scale_alto = [int(scala * i) for i in bmp.size]
        # normaliza los puntos
        x1 = int((printer_zise[0] - scale_ancho) / 2)
        y1 = int((printer_zise[1] - scale_alto) / 2)
        x2 = x1 + scale_ancho
        y2 = y1 + scale_alto
        dib.expose(hDC.GetHandleOutput())

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

        return


