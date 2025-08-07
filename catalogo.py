import pyautogui
import pygetwindow
import pyperclip
import time

from excel import abrir_excel, insere_produtos, ativar_janela
from print import processa_imagem, numero_loop
from nubimetrics import pesquisa_OEM

X_SOMA = 94
Y_SOMA = 12
Y_BORDA = 20 # Variavel para alteração de cada linha até a borda do catálogo

# def tempo(valor_tempo):
#     tempo_init = time.time()
#     while time.time() - tempo_init < valor_tempo:
#         pass

def abrir_catalogo(catalogo):

    cont = 0

    # Caso YM tenha sido selecionada no catálogo
    if catalogo == "YM":
        pyautogui.press("win")
        pyautogui.write("YM Distribuidora")
        pyautogui.press("enter")
        
        # Tempo de 8 segundos para fechar pop-up da YMax
        # Tempo pode ser alterado, vai de PC para PC
        time.sleep(8)

        # Sequência de 2 Enter pois a pesquisa ja vem selecionada
        # 1° Enter faz a pesquisa nula
        # 2° Enter confirma a pesquisa
        pyautogui.press("enter") 
        time.sleep(1)
        pyautogui.press("enter")

    if catalogo == "MRMK":
        pyautogui.press("win")
        pyautogui.write("MrMk")
        pyautogui.press("enter")

        # Move o mouse exatamente na posição do X
        # Para Fechar o Pop-Up
        # Aguarda o aplicativo ser aberto
        time.sleep(4)
        pyautogui.click(x=1299 ,y=208)

        # Sequência de 2 Enter pois a pesquisa ja vem selecionada
        # 1° Enter faz a pesquisa nula
        # 2° Enter confirma a pesquisa
        pyautogui.press("enter") 
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(7)

        # Chama a função para abrir e formatar o Excel
        abrir_excel()

        time.sleep(10)

        # Fazer loop para cópia de todo o Catálogo
        copiar_produto(catalogo, cont)
        
def copiar_produto(catalogo, cont):
    if catalogo == "YM":
        ...
    if catalogo == "MRMK":

        contagem = 0
        y_cont = 230

        num = numero_loop(catalogo)
        print(type(num), num)

        while contagem < num:

            pygetwindow.getWindowsWithTitle("MrMk")[0].activate()
            # pyautogui.click(x=657, y=1059)

            print(f"Cont: {cont} | ycont: {y_cont}")

            produto = []
            coordenada = processa_imagem() # Pega a posição do primeiro Código OEM
            pyautogui.click(x=coordenada[0], y=coordenada[1],button="right") # Codigo OEM
            pyautogui.click(x=coordenada[0] + X_SOMA, y=coordenada[1] + Y_SOMA) 
            produto.append(pyperclip.paste())  # Adiciona o valor copiado na ultima posição da lista
            pyautogui.click(x=402, y=y_cont, button="right") # Código Fabricante
            pyautogui.click(x=402 + X_SOMA, y=y_cont + Y_SOMA) # Copia o Código de Fabricante
            produto.append(pyperclip.paste()) # Adiciona o Código de Fabricante a lista
            pyautogui.click(x=1211, y=751, button="right") # Preço Fabricante
            pyautogui.click(x=1211 + X_SOMA, y=751 + Y_SOMA)
            time.sleep(0.1)
            pyautogui.click(x=260, y=460) # Clique aleatorio para focar na tela
            pyautogui.keyDown("down")
            time.sleep(0.1)
            pyautogui.keyUp("down")
            produto.append(pyperclip.paste()) # Adiciona o Preço a lista
            print(produto)

            if cont < 9:
                cont += 1
                y_cont += Y_BORDA

            pyautogui.click(x=605, y=1059)
            produto = pesquisa_OEM(produto[0], produto)
            pygetwindow.getWindowsWithTitle("Nubimetrics")[0].minimize()

            time.sleep(4)
            insere_produtos(produto)

            contagem += 1