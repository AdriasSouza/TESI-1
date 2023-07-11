import tkinter as tk
from tkinter import ttk


class Tela:
    def __init__(self, mestre):
        self.janela = mestre

        # seta uma scrollbar em janela e da grid nela ao lado do treeview
        self.scb = tk.Scrollbar(self.janela)
        self.scb.grid(row=0, column=1, sticky='ns')

        # configuração das colunas do treeview, com a associação ao scrollbar
        colunas = ('nome', 'telefone', 'email')
        tvw = ttk.Treeview(self.janela, columns=colunas, show='headings', yscrollcommand=self.scb.set)  # por padrão
        # vem como 'tree headings'
        tvw.grid(row=0, column=0)
        self.scb.config(command=tvw.yview)

        # Cabeçalho
        tvw.heading('nome', text='Nome')  # o nome do primeiro parametro tem que ser o mesmo do de cima
        tvw.heading('telefone', text='Telefone')
        tvw.heading('email', text='e-mail')

        # Colunas
        tvw.column('nome', minwidth=200, width=200)  # da pra configurar o tamanho da coluna
        tvw.column('telefone', minwidth=100, width=100)
        tvw.column('email', minwidth=300, width=300)

        tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['fulano', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['sicrano', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['beltrano', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['joao', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['pedro', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['paulo', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['ricardo', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['zeca', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['tio toin', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['padi ciço', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['so sei que foi assim', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['laine', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['adrias', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])



        # professores = tvw.insert('', 'end', text='Professores')
        # tvw.insert(professores, 'end', text='Limeira')
        # tvw.insert(professores, 'end', text='Fulano')

        """
        alunos = tvw.insert('', 'end', text='Alunos')
        tvw.insert(alunos, 0, text='Cicrano') # assim funciona como lista de prioridade
        tvw.insert(alunos, 'end', text='Beltrano')
        """


mestre = tk.Tk()
app = Tela(mestre)
mestre.mainloop()
