import pyautogui
import time
import tkinter as tk
from tkinter import ttk

class Servidores():
    def __init__(self,nome,ip,):
        self.nome = nome
        self.ip = ip

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
        super().__init__("Bosque", "xxxxxxxxxxxxx")

class Satelite(Servidores):
    def __init__(self):
        super().__init__("Satelite", "xxxxxxxxxxxxx")

class Matriz(Servidores):
    def __init__(self):
        super().__init__("Matriz", "xxxxxxxxxxxxx")

janela = tk.Tk()
janela.title("siganet")

Servidores = [
    Taubate(), Charles(), Caragua(), Jacarei(), Siqueira(), Vista_Verde(), Vila_Industrial(), Vila_Adyanna(), Bosque(), Satelite(), Matriz()
]

for servidor in Servidores:
    btn = tk.Button(
        janela, 
        text=servidor.nome, 
        width = 20, height = 2
    )
    btn.pack(pady=5)

janela.mainloop()


    