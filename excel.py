# Seção de Imports
import pyautogui
import pygetwindow
import time
import win32gui

pos_celula = 2

def abrir_excel():
    # Abrir o Excel
    pyautogui.press("win")
    pyautogui.write("Excel")
    pyautogui.press("enter")

    # Tempo de espera para o Excel abrir
    # e ser maximizado
    time.sleep(1)
    pygetwindow.getWindowsWithTitle("Excel")[0].maximize()

    time.sleep(6)

    pyautogui.click(x=271, y=212) # Inicia uma planilha em branco

    time.sleep(2.5)

    pyautogui.click(x=13, y=210) # Seleciona todos os itens da celula A
    pyautogui.click(x=455, y=86) # Centraliza os itens no eixo Y
    pyautogui.click(x=455, y=116) # Centraliza os itens no eixo X
    pyautogui.click(x=891, y=84) # Clica na caixa de "Geral"
    time.sleep(1)
    pyautogui.click(x=858, y=557) # Seleciona a formatação de "Texto"
    pyautogui.click(x=1544, y=95) # Clica no Botão de formatar
    time.sleep(1)
    pyautogui.click(x=1616, y=226) # Clica no Botão de alterar a largura
    pyautogui.write("20") # Aumenta a Largura da coluna para 20
    pyautogui.press("enter")
    pyautogui.click(x=533, y=217) # Coluna D - Titulo do Anuncio
    pyautogui.click(x=1544 ,y=95)
    time.sleep(1)
    pyautogui.click(x=1616, y=226)
    pyautogui.write("55.14")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'g')
    time.sleep(0.5)
    pyautogui.write("A1") # Vai pra Celula A1
    pyautogui.press("enter")

    infos = ["Codigo OEM", "Codigo Fabricante", "Preco Distribuidora", "Titulo do Anuncio", 
             "Preco Mercado Livre", "Dias Anunciados", "Premium / Classico", "Concorrente", "Quantidade Vendida"]

    # Função para inserir os Cabeçalhos de cada Coluna
    for info in infos:
        pyautogui.write(str(info))
        pyautogui.press("right")

    pyautogui.hotkey('ctrl', 'g')
    time.sleep(0.5)
    pyautogui.write("A2") # Deixa preparado na Celula A2
    pyautogui.press("enter")

    # Minimiza o Excel para realizar outras funções
    pygetwindow.getWindowsWithTitle("Pasta")[0].minimize()

def insere_produtos(produto):
    try:
        global pos_celula
        print(produto)
        pyautogui.click(x=362, y=1058)

        for coluna in produto:
            # print(info)
            pyautogui.write(str(coluna))
            pyautogui.press("right")

        pos_celula += 1
        pyautogui.hotkey('ctrl', 'g')  
        time.sleep(0.5)
        pyautogui.write(f"A{pos_celula}") # Na teoria, muda a celula conforme for preenchendo
        pyautogui.press("enter")
            
        # print("DEU CERTO, BASTA FAZER O LOOP")

    except TypeError:
        ...

def ativar_janela(titulo):
    janelad = pygetwindow.getWindowsWithTitle(titulo)
    if janelad:
        janela = janelad[0]._hWnd
        win32gui.ShowWindow(janela, 5) # Restaura a Janela
        win32gui.SetForegroundWindow(janela) # Traz para primeiro plano

        # Função para ver se o Excel ja foi aberto
        for _ in range(10):
            if win32gui.GetForegroundWindow() == janela:
                return True
            time.sleep(0.1)

    return False