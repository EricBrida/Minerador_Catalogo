# Sobre o código - Minerador_Catalogo

> [!IMPORTANT]
> *O Programa não irá rodar devido a necessidade de um **Catálogo IDEIA***</br>
> *e por **configurações de interface do Excel**.*

Programa feito para obter itens de um catálogo IDEIA e realizar uma busca na nubimetrics.


# Tecnologias Utilizadas

[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/docs)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/pt-br/3/)

### Dependências:
- **[Selenium](https://pypi.org/project/selenium/)**: Para automação de navegador.
- **[webdriver-manager](https://pypi.org/project/webdriver-manager/)**: Para gerenciar o ChromeDriver automaticamente
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Para carregar variáveis do .env.
- **[pytesseract](https://pypi.org/project/pytesseract/)**: Para leitura OCR de imagens, se você captura texto da tela
- **[pyautogui](https://pyautogui.readthedocs.io/en/latest/)**: Para automação de mouse e teclado
- **[pillow](https://pypi.org/project/pillow/)**: PyAutoGUI e pytesseract dependem disso
- **[pygetwindow](https://pypi.org/project/PyGetWindow/)**: Detectar ou manipular janelas
- **[pyperclip](https://pypi.org/project/pyperclip/)**: Acesso ao clipboard (copiar/colar texto)
- **[win32gui](https://pypi.org/project/win32gui/)**: Acesso à API gráfica do Windows
- **[tkinter](https://docs.python.org/3/library/tkinter.html)**: Interface gráfica (GUI)

> [!IMPORTANT]
> *É necessário ter instalado o **Tesseract-OCR**.*</br>
> *Pode ser obtido por meio deste link: **https://github.com/tesseract-ocr/tesseract***

# Como Utilizar

#### No terminal e no diretório de sua escolha, de o seguinte comando:
```
git clone https://github.com/EricBrida/Minerador_Catalogo.git
cd Minerador_Catalogo
```

#### Após a clonagem do repositório, é uma boa índole criar um ambiente virtual para a instalação das dependências:

> [!NOTE]
> ***.venv** ou **.env** são opções viáveis para o nome de seu ambiente virtual.* </br>
> *Você pode selecionar o ambiente virtual pelo atalho **CTRL + SHIFT + P**, procurar por **"Python: Select Interpreter"** e buscar pelo .exe do venv.* </br>
> *O comando "pip install -r requirements.txt" fará a instalação de todas as dependências utilizadas no projeto.*

```
python -m venv <nome_ambiente_virtual>
<nome_ambiente_virtual>\Scripts\activate
pip install -r requirements.txt
```

> [!IMPORTANT]
> *Para rodar a aplicação é necessário executar diretamente pelo arquivo **"main.py"**.*

#### Caso execute pelo terminal: 
```
python main.py
```

#### Caso tenha as extensões do Python baixada em seu VSCode:
<div>
    <img src="img/RUN_PYTHON.png">
</div>
 
### E-mail para contato: 
- **Eric Bueno Corrêa Brida** | *E-mail: [ericbrida.contato@gmail.com](mailto:ericbrida.contato@gmail.com)*
