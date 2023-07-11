import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
progresso = tk.IntVar()


def iniciar():
    prb.start(20)
    lbl['text'] = prb['value']
    lbl.after(100, iniciar)  # Recursividade
    if prb['value'] == 100:
        prb.stop()


# Progressbar
prb = ttk.Progressbar(janela, orient=tk.HORIZONTAL, mode='determinate', variable=progresso, maximum=100)
prb.pack()

# Label
lbl = tk.Label(janela, text='', bg='white', padx=10)
lbl.pack()

# Botões
btn_start = ttk.Button(janela, text='Start', command=iniciar)  # command=lambda: prb.start(10)
# Sem os parenteses o metodo só é acionado quando clicar
btn_start.pack()
btn_stop = ttk.Button(janela, text='Stop', command=prb.stop)
# Com os parenteses ele já começa acionado
btn_stop.pack()

janela.mainloop()
