import tkinter as tk
from tkinter import messagebox
import threading

def adicionar_entrada(valor):
    entrada.set(entrada.get() + valor)

def limpar_entrada():
    entrada.set("")

def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.set(str(resultado))
    except Exception as e:
        entrada.set("")
        messagebox.showerror("Erro", f"Expressão inválida: {str(e)}")

def calcular_thread():
    threading.Thread(target=calcular).start()

def teclado(event):
    tecla = event.char
    if tecla in "0123456789+-*/().":
        adicionar_entrada(tecla)
    elif tecla == "\r":
        calcular_thread()
    elif tecla == "\x08":
        entrada.set(entrada.get()[:-1])

root = tk.Tk()
root.title("Calculadora Multithreads")
root.geometry("300x400")
root.bind("<Key>", teclado)

entrada = tk.StringVar()

tk.Entry(root, textvariable=entrada, font=("Arial", 20), justify="right").pack(fill=tk.BOTH, pady=10)

botoes = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", ".", "+"),
]

for linha in botoes:
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for texto in linha:
        btn = tk.Button(
            frame,
            text=texto,
            font=("Arial", 18),
            command=(lambda t=texto: limpar_entrada() if t == "C" else adicionar_entrada(t))
        )
        btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tk.Button(root, text="=", font=("Arial", 18), bg="lightblue", command=calcular_thread).pack(fill=tk.BOTH, pady=10)

root.mainloop()
