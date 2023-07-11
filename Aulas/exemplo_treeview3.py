import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Tela:
    def __init__(self, mestre):
        self.janela = mestre

        # seta uma scrollbar em janela e da grid nela ao lado do treeview
        self.scb = tk.Scrollbar(self.janela)
        self.scb.grid(row=0, column=1, sticky='ns')

        # configuração das colunas do treeview, com a associação ao scrollbar
        colunas = ('nome', 'telefone', 'email')
        self.tvw = ttk.Treeview(self.janela, columns=colunas, show='headings',
                                yscrollcommand=self.scb.set)  # por padrão
        # vem como 'tree headings'
        self.tvw.grid(row=0, column=0)
        self.scb.config(command=self.tvw.yview)

        # Cabeçalho
        self.tvw.heading('nome', text='Nome')  # o nome do primeiro parametro tem que ser o mesmo do de cima
        self.tvw.heading('telefone', text='Telefone')
        self.tvw.heading('email', text='e-mail')

        # Colunas
        self.tvw.column('nome', minwidth=200, width=200)  # da pra configurar o tamanho da coluna
        self.tvw.column('telefone', minwidth=100, width=100)
        self.tvw.column('email', minwidth=300, width=300)

        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['fulano', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['sicrano', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['beltrano', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['joao', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['pedro', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['paulo', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['ricardo', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['zeca', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['tio toin', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['padi ciço', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['so sei que foi assim', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['laine', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['adrias', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])
        self.tvw.insert('', 'end', values=['Limeira', '99999', 'limeira@ufac.br'])

        # Botões
        frm_botoes = tk.Frame(self.janela)
        frm_botoes.grid(row=1, column=0)
        btn_cadastrar = tk.Button(frm_botoes, command=self.cadastrar, text='Cadastrar')
        btn_cadastrar.grid()
        btn_excluir = tk.Button(frm_botoes, command=self.excluir, text='Excluir')
        btn_excluir.grid()
        btn_editar = tk.Button(frm_botoes, command=self.atualizar, text='Atualizar')
        btn_editar.grid()

    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        telefone = self.ent_telefone.get()
        email = self.ent_email.get()
        if nome == '' or telefone == '' or email == '':
            messagebox.showinfo('Aviso', 'Preencha os dados corretamente', parent=self.top_cadastrar)
            return False
        self.tvw.insert('', 'end', values=(nome, telefone, email))
        self.top_cadastrar.destroy()

    # Funções
    def cadastrar(self):
        self.top_cadastrar = tk.Toplevel()
        self.top_cadastrar.title('Cadastrar')
        self.top_cadastrar.grab_set()
        lbl_nome = tk.Label(self.top_cadastrar, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self.top_cadastrar)
        self.ent_nome.grid(row=0, column=1)
        lbl_telefone = tk.Label(self.top_cadastrar, text='Telefone:')
        lbl_telefone.grid(row=1, column=0)
        self.ent_telefone = tk.Entry(self.top_cadastrar)
        self.ent_telefone.grid(row=1, column=1)
        lbl_email = tk.Label(self.top_cadastrar, text='E-mail:')
        lbl_email.grid(row=2, column=0)
        self.ent_email = tk.Entry(self.top_cadastrar)
        self.ent_email.grid(row=2, column=1)
        btn_confirmar = tk.Button(self.top_cadastrar, text='Confirmar', command=self.confirmar_cadastro)
        btn_confirmar.grid(row=3)

    def excluir(self):
        item = self.tvw.selection()
        print(item)
        if item == ():
            messagebox.showinfo('Aviso', 'Não há itens para serem excluidos!')
            return False
        for x in item:
            self.tvw.delete(x)

    def atualizar(self):
        item2 = self.tvw.selection()
        if len(item2) != 1:
            messagebox.showwarning('Aviso', 'Selecione apenas um item')
            return False
        valores = self.tvw.item(item2, 'values')
        self.top_atualizar = tk.Toplevel()
        self.top_atualizar.title('Editar')
        self.top_atualizar.grab_set()
        lbl_nome = tk.Label(self.top_atualizar, text='Nome:')
        lbl_nome.grid(row=0, column=0)
        self.ent_nome = tk.Entry(self.top_atualizar)
        self.ent_nome.grid(row=0, column=1)
        self.ent_nome.insert('end', valores[0])
        lbl_telefone = tk.Label(self.top_atualizar, text='Telefone:')
        lbl_telefone.grid(row=1, column=0)
        self.ent_telefone = tk.Entry(self.top_atualizar)
        self.ent_telefone.grid(row=1, column=1)
        self.ent_telefone.insert('end', valores[1])
        lbl_email = tk.Label(self.top_atualizar, text='E-mail:')
        lbl_email.grid(row=2, column=0)
        self.ent_email = tk.Entry(self.top_atualizar)
        self.ent_email.grid(row=2, column=1)
        self.ent_email.insert('end', valores[2])
        btn_confirmar = tk.Button(self.top_atualizar, text='Confirmar', command=self.confirmar_edicao)
        btn_confirmar.grid(row=3)

    def confirmar_edicao(self):
        nome = self.ent_nome.get()
        telefone = self.ent_telefone.get()
        email = self.ent_email.get()
        selecionado = self.tvw.selection()
        if nome == '' or telefone == '' or email == '':
            messagebox.showinfo('Aviso', 'Preencha os dados corretamente', parent=self.top_cadastrar)
            return False
        self.tvw.item('', selecionado, values=(nome, telefone, email))
        self.top_cadastrar.destroy()

        # professores = self.insert('', 'end', text='Professores')
        # tvw.insert(professores, 'end', text='Limeira')
        # tvw.insert(professores, 'end', text='Fulano')

        """
        alunos = tvw.insert('', 'end', text='Alunos')
        tvw.insert(alunos, 0, text='Cicrano') # assim funciona como lista de prioridade
        tvw.insert(alunos, 'end', text='Beltrano')
        """


# Fazer botão pesquisar
mestre = tk.Tk()
app = Tela(mestre)
mestre.mainloop()
