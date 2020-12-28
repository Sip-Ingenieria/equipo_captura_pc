import os, sys
import win32print,win32ui,win32con
from PIL import Image
import base64

#img = Image.open("./13-03-emoji-marketing-1280x720.png")
#img.show()
with open ("./13-03-emoji-marketing-1280x720.png","rb") as imagenfile:
    imagen = base64.b64encode(imagenfile.read())
    print (type(imagen))
INCH = 1140
#crea un objeto PDF
hDC = win32ui.CreateDC()
#configura la impresora por defecto
hDC.CreatePrinterDC(win32print.GetDefaultPrinter())
#crea el archivo
hDC.StartDoc('file name10')
#inicia la pagina
hDC.StartPage()
#asigna modo de mapeo
hDC.SetMapMode(win32con.MM_TWIPS)
#escribe una cadena en un rectangulo con un formato
hDC.DrawText(str(imagen),(0,INCH*-1,INCH*8,INCH*-2),win32con.DT_CENTER)
#hDC.DrawIcon((0,INCH*10),imagen)
#termina la pagina
hDC.EndPage()
#termina el documento
hDC.EndDoc()

