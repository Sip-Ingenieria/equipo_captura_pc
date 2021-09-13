import socket
import traceback
import os


def etiqueta(nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades, ancho, largo,  codigo ):
    message = b"^XA" \
             b"^FO30, 40^ADN, 61, 33^FD %s ^FS" \
             b"^FO500, 20^ADN 11, 7^FD # ETIQUETA ^FS" \
             b"^FO555, 40^ADN, 20, 11^FD %s ^FS" \
             b"^FO30, 110^ADN 26, 11^FD CODIGO: ^FS" \
             b"^FO120, 110^ADN, 26, 11^FD %s ^FS" \
             b"^FO270, 110^ADN, 26,11^FD PED: ^FS" \
             b"^FO330, 110^ADN, 26, 11^FD %s ^FS" \
             b"^FO500, 110^ADN, 26, 11^FD OT: ^FS" \
             b"^FO550, 110^ADN, 26, 11^FD %s ^FS" \
             b"^FO100, 150^ADN, 26, 11^FD CANTIDAD: ^FS" \
             b"^FO220, 150^ADN, 36, 20^FD %s ^FS" \
             b"^FO400, 150^ADN, 26, 11^FD PESO: ^FS" \
             b"^FO500, 150^ADN, 36, 20^FD %s%s ^FS" \
             b"^FO100, 200^ADN. 26, 11^FD ANCHO: ^FS" \
             b"^FO220, 200^ADN, 36, 20^FD %s ^FS" \
             b"^FO400, 200^ADN. 26, 11^FD LARGO: ^FS" \
             b"^FO500, 200^ADN, 36, 20^FD %s ^FS" \
             b"^FO200, 270^ADN, 36, 20" \
             b"^BQN, 2, 10" \
             b"^FD %s^FS" \
             b"^XZ" % (nombre_empresa, n_etiqueta, testo, descripcion, ot, cantidad, peso, unidades, ancho, largo, codigo)

    return message


print 'here'
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
pot = 9100
nombre_empresa = 'ICOMALLAS'
codigo = 123456789
pedido = 'PF004600'
OT = '156-789'
referencia = 'E x R xxxxxxxx'
cantidad = 500
peso = 78
ancho = 1.25
largo = 1.25
n_etiqueta = 150
print etiqueta(nombre_empresa, n_etiqueta, codigo, pedido, OT, cantidad, peso, 'kg', ancho, largo, 12345678901)

try:
    mysocket.connect((host, pot))
    mysocket.send(etiqueta(nombre_empresa, n_etiqueta, codigo, pedido, OT, cantidad, peso, 'kg', ancho, largo, 12345678901))
    mysocket.close()
    ruta_actual = os.getcwd()
    nombre_archivo = "LBL000000.png"
    ruta_documento = "%s\%s" % (ruta_actual, nombre_archivo)
    os.startfile(ruta_documento, "print")

except:
    print 'Error de comunicacion: %s' % traceback.format_exc()