# Seção de imports para funcionamento do código

# Selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException

import pyautogui

# Dotenv e OS
from dotenv import load_dotenv
import os

import time

# Função para carregar as variáveis de ambiente
# de Usuário e Senha para acesso da Nubimetrics
load_dotenv()

# Adicionando opção de detach ao chrome para que o navegador
# não feche ao script ser finalizado
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Definindo as variável de LINK
# e as variáveis de USER e PSW 
LINK = 'https://app.nubimetrics.com/account/login?'
USER = os.getenv('USER')
PSW = os.getenv('PASSWORD')

# Função para abrir a Nubimetrics,
# e chamar a função realizar_login
def iniciando_nubi():
    try:
        print("Iniciando o Selenium...")
        service = Service(ChromeDriverManager().install())
        global driver 
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(LINK)
        driver.maximize_window()
        print("Página carregada!")
        realizar_login()
    except Exception as e:
        print(f"Erro ao iniciar o Selenium: {e}")

# Função para realizar o login na Nubimetrics, 
# via ID e XPath
def realizar_login():
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
    except Exception as e:
        print(f"Erro ao tentar proceder com o login: {e}")
    finally:
        driver.find_element(By.ID, "email").send_keys(USER)
        driver.find_element(By.ID, "password").send_keys(PSW)
        driver.find_element(By.XPATH, '//*[@id="contenido"]/form/button').click()

def pesquisa_OEM(oem, produto):
    try:
        for i in range(30):
            driver.find_element(By.ID, "ex1_value").send_keys(Keys.BACK_SPACE)

        driver.find_element(By.ID, "ex1_value").send_keys(oem) # pesquisa o Código OEM na Nubimetrics
            
        espera = WebDriverWait(driver, 12) # Tempo pode ser ajustado
        espera.until(EC.invisibility_of_element_located((By.ID, "background-container")))

        botao = espera.until(EC.element_to_be_clickable((By.ID, "btn-search")))
        botao.click()

        # Tempo de 8 segundos para realizar a pesquisa
        time.sleep(8)

        espera.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[2]/ul/li/a")))

        copia = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[2]/ul/li/a") # Titulo do Anuncio
        produto.append(copia.text)
        copia = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[3]") # Preço do Anuncio
        produto.append(copia.text)
        copia = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[4]/ul/li/span") # Dias Anunciados
        produto.append(copia.text)
        copia = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[5]/ul/li[2]/div[2]") # Premium / Classico
        produto.append(copia.text)
        copia = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[5]/ul/li[1]/div[2]/a") # Concorrente
        produto.append(copia.text)
        time.sleep(0.5)
        espera.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[3]/section/div[2]/div/table/tbody/tr[1]/td[2]/ul/li/a")))
        pyautogui.middleClick(x=678, y=565)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', '2')
        driver.switch_to.window(driver.window_handles[1])
        copia = driver.find_element(By.CLASS_NAME, "ui-pdp-subtitle") # Quantidade Vendida
        produto.append(copia.text)
        print(produto)
        pyautogui.click(x=493, y=18)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(0.5)

        return produto
    
    except (NoSuchElementException, StaleElementReferenceException, WebDriverException, TypeError):
        print("Elemento Não Localizado")
        for _ in range(9 - len(produto)):
            produto.append("N/A")
        return produto 

    except Exception as e:
        print("Elemento Não Localizado")
        for _ in range(9 - len(produto)):
            produto.append("N/A")
        return produto 