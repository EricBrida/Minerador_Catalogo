# Seção de Imports para tratamento de imagem

import pyautogui
from PIL import Image
import pytesseract

X = 297
Y = 501

def processa_imagem():
    area = (297, 501, 165, 228)

    # Tira uma print da região dos códigos OEM
    screen = pyautogui.screenshot(region=area)
    img = screen.convert('RGB')

    # Função que verifica a cor alvo
    def verifica_cor(cor_pixel):
        r, g, b = cor_pixel
        return r < 50 and g < 50 and b < 50
        

    # RGB da cor preta
    cor_desejada = (0, 0, 0)

    menorx = X
    menory = Y

    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            cor_pixel = pixels[x, y]
            if verifica_cor(cor_pixel):
                # print(f"Cor encontrada no pixel ({x}, {y})")
                if x < menorx:
                    menorx = x
                if y < menory:
                    menory = y
            
    coordenada = [menorx + X, menory + Y]

    # texto = str(pytesseract.image_to_string(img))
    # print(f"Texto extraido: {texto}")
    return coordenada

def numero_loop(catalogo):

    # Usar o tesseract para pegar a quantidade de produtos no catalogos para loop
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

    if catalogo == "YM":
        ...
    if catalogo == "MRMK":
        area = (1241, 426, 39, 14)

        imagem = pyautogui.screenshot(region=area)
        img = imagem.convert('RGB')

        try:
            resultado = pytesseract.image_to_string(img, config='--psm 6')
            num = resultado.replace(".", "").replace(",", "").replace("\n", "")
            num = int(num)
            print(num)
            return num
        except Exception as e:
            print(f"Não foi possivel realizar a captura de loop. {e}")