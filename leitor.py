import tkinter as tk
import threading
import time

def contar_sem_threads():
    resultado.delete("1.0", tk.END)
    inicio = time.perf_counter()
    total_palavras = sum(len(parte.split()) for parte in partes)
    fim = time.perf_counter()
    resultado.insert(tk.END, "Texto dividido em 3 partes:\n")
    resultado.insert(tk.END, f"Parte 1: {partes[0]}\n\n")
    resultado.insert(tk.END, f"Parte 2: {partes[1]}\n\n")
    resultado.insert(tk.END, f"Parte 3: {partes[2]}\n\n")
    resultado.insert(tk.END, f"Total de palavras: {total_palavras}\n")
    resultado.insert(tk.END, f"Tempo sem Threads: {fim - inicio:.4f} segundos\n")

def contar_com_threads():
    global inicio
    resultado.delete("1.0", tk.END)
    inicio = time.perf_counter()
    threading.Thread(target=contar_palavras_com_threads).start()

def contar_palavras_com_threads():
    global inicio
    resultados = [0] * 3
    threads = []
    for i, parte in enumerate(partes):
        thread = threading.Thread(target=lambda p, r, idx: r.insert(idx, len(p.split())), args=(parte, resultados, i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    total_palavras = sum(resultados)
    resultado.insert(tk.END, "Texto dividido em 3 partes:\n")
    resultado.insert(tk.END, f"Parte 1: {partes[0]}\n\n")
    resultado.insert(tk.END, f"Parte 2: {partes[1]}\n\n")
    resultado.insert(tk.END, f"Parte 3: {partes[2]}\n\n")
    resultado.insert(tk.END, f"Total de palavras: {total_palavras}\n")
    fim = time.perf_counter()
    resultado.insert(tk.END, f"Tempo com Threads: {fim - inicio:.4f} segundos\n")

texto = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
           Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
           It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
partes = texto.split('. ')
partes = [' '.join(partes[:len(partes)//3]), ' '.join(partes[len(partes)//3:2*len(partes)//3]), ' '.join(partes[2*len(partes)//3:])]

root = tk.Tk()
root.title("Contagem de Palavras")

tk.Button(root, text="Contar sem Threads", command=contar_sem_threads).pack()
tk.Button(root, text="Contar com Threads", command=contar_com_threads).pack()

resultado = tk.Text(root, wrap=tk.WORD, width=80, height=20)
resultado.pack()

root.mainloop()
