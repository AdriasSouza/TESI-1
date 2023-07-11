import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, mestre):
        self.janela = mestre

        tvw = ttk.Treeview(self.janela)
        tvw.pack()
        professores = tvw.insert('', 'end', text='Professores')
        tvw.insert(professores, 'end', text='Limeira')
        tvw.insert(professores, 'end', text='Fulano')

        alunos = tvw.insert('', 'end', text='Alunos')
        tvw.insert(alunos, 0, text='Cicrano') # assim funciona como lista de prioridade
        tvw.insert(alunos, 'end', text='Beltrano')



mestre = tk.Tk()
app = Tela(mestre)
mestre.mainloop()