import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import simpledialog
import os

class Servidores():
    def __init__(self,nome,ip,):
        self.nome = nome
        self.ip = ip

    def executar_automacao(self):
        time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
       super().__init__("nome da unidade", "ip da unidade")
def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")

    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1) 
        

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)

class #nome da unidade(Servidores):
    def __init__(self):
        super().__init__("#nome da unidade", "ip da unidade")
    def executar_automacao(self):
        def obter_numero_guiche():
            root = tk.Tk()
            root.withdraw()
            try:
                while True:
                    numero_guiche = simpledialog.askstring(
                        "escolha do guichê",
                        "digite o numero de (01 a 21)",
                    )
                    if numero_guiche is None:
                        return None
                    if numero_guiche.isdigit() and 1 <= int(numero_guiche) <= 21:
                        return numero_guiche.zfill(2)
            finally:
                root.destroy()

        numero_guiche = obter_numero_guiche()   
        if numero_guiche is None:
            print("nenhum numero foi slecionado, automação falhou")
            return
                
        time.sleep(1)
        pyautogui.hotkey("win","r")
        time.sleep(0.5)
        pyautogui.write("caminho do executavel do software")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        for _ in range(6):
            pyautogui.press("tab")
            time.sleep(0.2)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(3):
            pyautogui.press("tab")
            time.sleep(0.2)
        pyautogui.write(str(numero_guiche))
        time.sleep(1)
        for _ in range(4):
            pyautogui.press("tab")
            time.sleep(0.2)

        pyautogui.write(self.ip)
        time.sleep(0.5)
        for _ in range(2):
            pyautogui.press("up")
            time.sleep(0.2)

        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.press("left")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("down")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("right")
        time.sleep(1)
        for _ in range(5):
            pyautogui.press("up")
            time.sleep(0.2)
        for _ in range(3):
            pyautogui.press("left")
            time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("left")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        for _ in range(2):
            pyautogui.press("right")
            time.sleep(1)
        
caminho_execuatvel = "caminho\executavel"

processo = subprocess.Popen(caminho_execuatvel)
time.sleep(7)
for _ in range(6):
    pyautogui.press("enter")

time.sleep(15)


janela = tk.Tk()
janela.title("siganet")

Servidores = [
    #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade(), #nome da unidade()
]

def criar_botao(Servidor):
    btn = tk.Button(
        janela, 
        text=servidor.nome, 
        width = 20, height = 2,
        command=lambda s=servidor: s.executar_automacao()
    )
    btn.pack(pady=5)

for servidor in Servidores:
    criar_botao(servidor)

janela.mainloop()





    
