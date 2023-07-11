import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry('300x250')

tk.Label(janela, text="Selecione o dia:").pack()
n = tk.StringVar()

# lista = ['Segunda', 'Terça', 'Quarta'] pode fazer assim e declaras values=lista no combobox
cbx = ttk.Combobox(janela, width=12, textvariable=n, state='readonly')
cbx['values'] = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')
cbx.current(1)
# cbx.set('Segunda')
cbx.pack()

janela.mainloop()
