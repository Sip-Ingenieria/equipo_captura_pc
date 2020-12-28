from PIL import ImageDraw,Image,ImageWin,ImageFont
import win32ui
import win32print

# #crear etiqueta
# tamano_tablero = 180
# ancho1=179
# ancho2=89
# alto1=45
# alto2=90
# alto3=135
# alto4=179
# imagen=Image.new('L',((tamano_tablero*6),(tamano_tablero*3)),color=(0))
# cuadrado = ImageDraw.Draw(imagen)
# cuadrado.rectangle([0,0,ancho1*6,alto1*3],fill='white',outline='black',width=1)
# cuadrado.rectangle([0,alto1*3,ancho1*6,alto2*3],fill='white',outline='black',width=1)
# cuadrado.rectangle([0,alto2*3,ancho2*6,alto3*3],fill='white',outline='black',width=1)
# cuadrado.rectangle([ancho2*6,alto2*3,ancho1*6,alto3*3],fill='white',outline='black',width=1)
# cuadrado.rectangle([0,alto3*3,ancho1*6,alto4*3],fill='white',outline='black',width=1)
#
# #texto
#
# fuente = ImageFont.load_default()
# print fuente
# cuadrado.text((0,30),'prueba etiqueta',fill='black',font=fuente)
#
#
# # def texto_etiqueta(texto):
# #     fuente = ImageFont.load('arial.pil')
# #     cuadrado.text((0,ancho1*3),'prueba etiqueta',fill=(255),font=fuente)
# #     return cuadrado
#
#
#
# #IMPRESION
# HORZRES = 8
# VERTRES = 10
#
# LOGPIXELSX=88
# LOGPIXELSY=90
#
# ANCHO_FISICO=110
# ALTO_FISICO=111
#
# OFSET_FISICO_X=112
# OFSET_FISICO_Y=112
#
# printer_name =win32print.GetDefaultPrinter()
# #file_name = './13-03-emoji-marketing-1280x720.png'
#
# hDC = win32ui.CreateDC()
# hDC.CreatePrinterDC(printer_name)
# printer_area= hDC.GetDeviceCaps(HORZRES),hDC.GetDeviceCaps(VERTRES)
#
# printer_zise = hDC.GetDeviceCaps(ANCHO_FISICO),hDC.GetDeviceCaps(ALTO_FISICO)
#
# printer_margin = hDC.GetDeviceCaps(OFSET_FISICO_X),hDC.GetDeviceCaps(OFSET_FISICO_Y)
#
# bmp= imagen
# #resolucion de la imagen,rotar para que encaje
# # if bmp.size[0] > bmp.size[1]:
# #
# #     bmp = bmp.rotate(90)
# #normalizar segun la resolucion de la imagen
# ratios = [1.0*printer_area[0]/bmp.size[0],1.0*printer_area[1]/bmp.size[1]]
#
# scala = min(ratios)
#
# hDC.StartDoc('3')
# hDC.StartPage()
#
# dib = ImageWin.Dib(bmp)
# scale_ancho,scale_alto =[int(scala*i) for i in bmp.size]
# print(scale_alto)
# print(scale_ancho)
# #normaliza los puntos
# x1 = int((printer_zise[0]-scale_ancho)/2)
# print(x1)
# y1 = int((printer_zise[1]- scale_alto)/2)
# print(y1)
# x2 = x1 + scale_ancho
# print(x2)
# y2 = y1 + scale_alto
# print(y2)
# dib.expose(hDC.GetHandleOutput())
#
# hDC.EndPage()
# hDC.EndDoc()
# hDC.DeleteDC()

##CREAR ETIQUETA###
def estructura_etiqueta():
    tamano_tablero = 180
    ancho1 = 179
    ancho2 = 89
    alto1 = 45
    alto2 = 90
    alto3 = 135
    alto4 = 179
    etiqueta = Image.new('L', ((tamano_tablero * 6), (tamano_tablero * 3)), color=(0))
    forma_etiqueta = ImageDraw.Draw(etiqueta)
    forma_etiqueta.rectangle([0, 0, ancho1 * 6, alto1 * 3], fill='white', outline='black', width=1)
    forma_etiqueta.rectangle([0, alto1 * 3, ancho1 * 6, alto2 * 3], fill='white', outline='black', width=1)
    forma_etiqueta.rectangle([0, alto2 * 3, ancho2 * 6, alto3 * 3], fill='white', outline='black', width=1)
    forma_etiqueta.rectangle([ancho2 * 6, alto2 * 3, ancho1 * 6, alto3 * 3], fill='white', outline='black', width=1)
    forma_etiqueta.rectangle([0, alto3 * 3, ancho1 * 6, alto4 * 3], fill='white', outline='black', width=1)

    return etiqueta

##AGREGAR TEXTO A LA ETIQUETA###
def agregar_texto_etiqueta(texto,coordenada):

    etiqueta=estructura_etiqueta()
    etiqueta_texto = ImageDraw.Draw(etiqueta)
    fuente = ImageFont.load_default()

    etiqueta_texto.text(coordenada,texto,fill='black',font=fuente)

    return etiqueta

##IMPRIMIR ETIQUETA###
def imprimir(etiqueta):
    HORZRES = 8
    VERTRES = 10

    LOGPIXELSX = 88
    LOGPIXELSY = 90

    ANCHO_FISICO = 110
    ALTO_FISICO = 111

    OFSET_FISICO_X = 112
    OFSET_FISICO_Y = 112

    printer_name = win32print.GetDefaultPrinter()
    # file_name = './13-03-emoji-marketing-1280x720.png'

    hDC = win32ui.CreateDC()
    hDC.CreatePrinterDC(printer_name)
    printer_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)

    printer_zise = hDC.GetDeviceCaps(ANCHO_FISICO), hDC.GetDeviceCaps(ALTO_FISICO)

    printer_margin = hDC.GetDeviceCaps(OFSET_FISICO_X), hDC.GetDeviceCaps(OFSET_FISICO_Y)

    #aqui se agrega la etiqueta
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
    print(scale_alto)
    print(scale_ancho)
    # normaliza los puntos
    x1 = int((printer_zise[0] - scale_ancho) / 2)
    print(x1)
    y1 = int((printer_zise[1] - scale_alto) / 2)
    print(y1)
    x2 = x1 + scale_ancho
    print(x2)
    y2 = y1 + scale_alto
    print(y2)
    dib.expose(hDC.GetHandleOutput())

    hDC.EndPage()
    hDC.EndDoc()
    hDC.DeleteDC()

    return

coordena = (0,180)

etiqueta = agregar_texto_etiqueta('prueba',coordena)

imprimir(etiqueta)