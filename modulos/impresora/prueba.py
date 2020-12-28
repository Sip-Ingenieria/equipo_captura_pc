from PIL import Image, ImageDraw, ImageFont
import cv2

def generar_imagen_letra(letra, tamano, fuente, tamano_tablero=100, limites=(50, 50)):
    # print("generar_imagen_letra: %s" % str(limites))
    offset = 10
    img = Image.new('L', (tamano_tablero, tamano_tablero), color=(0))
    fnt = ImageFont.truetype('%s/%s' % (DIRECTORIO_FUENTES, fuente), tamano)
    d = ImageDraw.Draw(img)

    d.text((offset, offset), letra, font=fnt, fill=(255))
    # img.save('temp.webp', "WEBP", optimize=True)
    # print("img: %s" % img)
    original_image = np.array(img)
    # print("original_image")
    # print("%s" % original_image)
    # print("open_cv_image: %s" % open_cv_image)
    # original_image = cv2.imread("temp.webp", cv2.IMREAD_GRAYSCALE)

    #cv2.imshow("original_image", original_image)
    #cv2.waitKey(0)

    return original_image