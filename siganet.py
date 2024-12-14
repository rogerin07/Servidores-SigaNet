import pyautogui
import time
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter import simpledialog
import os
import keyboard

class Servidores():
    def __init__(self,nome,ip,):
        self.nome = nome
        self.ip = ip

    def executar_automacao(self):
        time.sleep(1)

class Taubate(Servidores):
    def __init__(self):
        super().__init__("Taubate", "xxxxxxxxxxxxx")

class Charles(Servidores):
    def __init__(self):
        super().__init__("Charles", "xxxxxxxxxxxxx")

class Caragua(Servidores):
    def __init__(self):
       super().__init__("Caragua", "xxxxxxxxxxxxx")

class Jacarei(Servidores):
    def __init__(self):
        super().__init__("Jacarei", "xxxxxxxxxxxxx")

class Siqueira(Servidores):
    def __init__(self):
        super().__init__("Siqueira", "xxxxxxxxxxxxx")

class Vista_Verde(Servidores):
    def __init__(self):
        super().__init__("Vista_Verde", "xxxxxxxxxxxxx")

class Vila_Industrial(Servidores):
    def __init__(self):
        super().__init__("Vila_Industrial", "xxxxxxxxxxxxx")

class Vila_Adyanna(Servidores):
    def __init__(self):
        super().__init__("Vila_Adyanna", "xxxxxxxxxxxxx")

class Bosque(Servidores):
    def __init__(self):
        super().__init__("Bosque", "10.32.38.124")

    def capturar_coordenadas_ao_entrar(self):
        x, y = pyautogui.position()
        return x, y

    def mover_mouse_para_posicao(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()

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
        pyautogui.write("C:\\Program Files (x86)\\SigaNET\\configwindow.exe")
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

        pyautogui.press("enter")
        x, y = self.capturar_coordenadas_ao_entrar()
        self.mover_mouse_para_posicao(x, y)

        time.sleep(1)


        
        


class Satelite(Servidores):
    def __init__(self):
        super().__init__("Satelite", "xxxxxxxxxxxxx")

class Matriz(Servidores):
    def __init__(self):
        super().__init__("Matriz", "xxxxxxxxxxxxx")
        
caminho_execuatvel = "\\\\10.32.0.236\\Babkup\\TI\\SigaNET Atendeten.exe"

processo = subprocess.Popen(caminho_execuatvel)
time.sleep(7)
for _ in range(6):
    pyautogui.press("enter")

time.sleep(15)

    






janela = tk.Tk()
janela.title("siganet")

Servidores = [
    Taubate(), Charles(), Caragua(), Jacarei(), Siqueira(), Vista_Verde(), Vila_Industrial(), Vila_Adyanna(), Bosque(), Satelite(), Matriz()
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





    
