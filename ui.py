# Seção de imports para Interface Gráfico

import tkinter as tk
from catalogo import *

class UI:
    def __init__(self, root):
        self.root = root

        # Define o tamanho da janela de seleção de catalogo
        # e seu respectivo nome
        self.root.geometry("500x350")
        self.root.title("PythonBot")

        tk.Label(self.root, text="PythonBot", font=("Helvetica 16 bold")).pack(pady=10)
        tk.Label(self.root, text="Selecione um Catálogo:", font=("Helvetica 10")).pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.ctl = self.selecionar_catalogo()
        tk.Label(root, text="").pack(pady=10)
        tk.Label(root, text="Lembre-se de atualizar o catálogo antes de executar", font=("Helvetica 10 bold")).pack()
        tk.Button(root, text="Executar", font=("Helvetica 12"), command=self.receber_catalogo).pack()

    # Funções para a Interface

    def selecionar_catalogo(self):
        opt = tk.StringVar()
        menu_ctl = ['YM', 'MrMk']
        opt.set(menu_ctl[0])
        tk.OptionMenu(self.frame, opt, *menu_ctl).pack(side="left")
        return opt

    def receber_catalogo(self):
        self.catalogo = self.ctl.get().upper()
        self.root.destroy()
        return self.catalogo
    
    def chamar_catalogo(self, catalogo):
        if catalogo:
            print(catalogo)
            abrir_catalogo(catalogo)

def criar_ui():
    root = tk.Tk()
    app = UI(root)
    root.mainloop()
    app.chamar_catalogo(app.catalogo)