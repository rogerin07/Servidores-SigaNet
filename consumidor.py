import tkinter as tk
import threading
import time
import random
from collections import deque

def iniciar_sem_threads():
    buffer.clear()
    lista_buffer.delete(0, tk.END)
    inicio = time.perf_counter()
    for _ in range(tamanho_buffer.get()):
        numero = random.randint(1, 100)
        buffer.append(numero)
        lista_buffer.insert(tk.END, f"Produzido: {numero}")
    while buffer:
        numero = buffer.popleft()
        lista_buffer.insert(tk.END, f"Consumido: {numero}")
    fim = time.perf_counter()
    tempo_execucao.set(f"Tempo sem Threads: {fim - inicio:.4f} segundos")

def iniciar_com_threads():
    buffer.clear()
    lista_buffer.delete(0, tk.END)
    threading.Thread(target=produzir_consumir_com_threads).start()

def produzir_consumir_com_threads():
    inicio = time.perf_counter()
    for _ in range(tamanho_buffer.get()):
        numero = random.randint(1, 100)
        buffer.append(numero)
        lista_buffer.insert(tk.END, f"Produzido: {numero}")
        time.sleep(0.1)
    while buffer:
        numero = buffer.popleft()
        lista_buffer.insert(tk.END, f"Consumido: {numero}")
        time.sleep(0.1)
    fim = time.perf_counter()
    tempo_execucao.set(f"Tempo com Threads: {fim - inicio:.4f} segundos")

root = tk.Tk()
root.title("Produtor-Consumidor")

buffer = deque()
tamanho_buffer = tk.IntVar(value=10)
tempo_execucao = tk.StringVar(value="Tempo: ")

tk.Label(root, text="Tamanho do Buffer:").pack()
tk.Entry(root, textvariable=tamanho_buffer).pack()
tk.Button(root, text="Executar sem Threads", command=iniciar_sem_threads).pack()
tk.Button(root, text="Executar com Threads", command=iniciar_com_threads).pack()
tk.Label(root, textvariable=tempo_execucao, fg="blue").pack()

lista_buffer = tk.Listbox(root, width=50, height=15)
lista_buffer.pack()

root.mainloop()
