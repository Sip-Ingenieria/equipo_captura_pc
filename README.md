# equipo_captura_pc
Emulador de equipo de captura en pc con servicio de impresion en impresora Zebra a traves de comandos ZPL

Requisitos:

Probado en python 3.7, pip 10.1

pip install ...
pyserial
zpl
pywin32
websocket-client

_En win7 requiere visual studio 14.0 o superior con compiladores

INF:

EL modulo bascula busca un puerto serial disponible y se conecta al primero que encuentre, luego escribe un arhivo en la ruta especificada

El modulo impresora busca la impresora llamada ZDesigner ZT230-300dpi ZPL, esta se instala a traves de su controlador propio, preferiblemente. Importante ZPL 

configurar a:
darkness 15 # superior si se ve requerido
vel 50
orientacion normal

CONFIG:

Configurar configuracion.py

RUTA_ARCHIVO = 'C:/EXAMPLE/EXAMPLE.txt' #ruta archivo leido

Ajustar MAC: '00:11:22:33:44:55' # MAC del equipo que tiene la bascula

Ajustar USUARIO ID: 1 # Debe concordar con el usuario de la interface web


