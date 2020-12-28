import win32ui
import win32print
from PIL import Image,ImageWin

HORZRES = 8
VERTRES = 10

LOGPIXELSX=88
LOGPIXELSY=90

ANCHO_FISICO=110
ALTO_FISICO=111

OFSET_FISICO_X=112
OFSET_FISICO_Y=112

printer_name =win32print.GetDefaultPrinter()
file_name = './13-03-emoji-marketing-1280x720.png'

# hDC = win32ui.CreateDC()
# hDC.CreatePrinterDC(printer_name)
# printer_area= hDC.GetDeviceCaps(HORZRES),hDC.GetDeviceCaps(VERTRES)
# print('el area de impresion es: %s %s' % printer_area)
# printer_zise = hDC.GetDeviceCaps(ANCHO_FISICO),hDC.GetDeviceCaps(ALTO_FISICO)
# print('el tamaño de impresion es: %s %s' % printer_zise)
# printer_margin = hDC.GetDeviceCaps(OFSET_FISICO_X),hDC.GetDeviceCaps(OFSET_FISICO_Y)
# print('el margen de impresion es: %s %s' % printer_margin)
# bmp= Image.open(file_name)
# #resolucion de la imagen,rotar para que encaje
# if bmp.size[0] > bmp.size[1]:
#     print('bmp.size[0] es %s' % bmp.size[0])
#     print('bmp.size[1] es %s' % bmp.size[1])
#     bmp = bmp.rotate(90)
# #normalizar segun la resolucion de la imagen
# ratios = [1.0*printer_area[0]/bmp.size[0],1.0*printer_area[1]/bmp.size[1]]
# print('ratios %s' % ratios)
# scala = min(ratios)
#
# hDC.StartDoc(file_name+'3')
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
# dib.draw(hDC.GetHandleOutput(),(x1,y1,x2,y2))
#
# hDC.EndPage()
# hDC.EndDoc()
# hDC.DeleteDC()