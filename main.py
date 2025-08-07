# Import no time

import time

# Seção de imports para modularizar o código
# e facilitar sua compreensão

from nubimetrics import iniciando_nubi
from ui import criar_ui
# from print import numero_loop

# If básico para rodar o código apenas
# executando o arquivo main.py
if __name__ == "__main__":
    iniciando_nubi()
    time.sleep(8)
    criar_ui()