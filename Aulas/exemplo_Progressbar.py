import tkinter as tk
from tkinter import ttk
import threading
import time

# Parametros da Janela
janela = tk.Tk()
janela.geometry('300x100')
janela.title('Progressbar')
p = tk.IntVar()
p.set(0)


# Funções da janela
def thread():
    th = threading.Thread(target=iniciar)  # parenteses exucuta antes de clicar no botão
    th.start()


def iniciar():
    for i in range(101):
        p.set(i)
        lbl['text'] = prb['value']
        time.sleep(0.1)
    # prb.start(10)
    # prb.step(10)


def parar():
    prb.stop()


# Elementos da Janela
prb = ttk.Progressbar(janela, orient='horizontal', variable=p, mode='indeterminate', maximum=100)
prb.pack()

btn_start = ttk.Button(janela, text='Start', command=iniciar)
btn_start.pack()

btn_stop = ttk.Button(janela, text='Stop', command=parar)
btn_stop.pack()

lbl = tk.Label(janela, text='0%')
lbl.pack()

janela.mainloop()
