import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Exemplo Text com Scrollbar')
        self.janela.geometry('400x400')

        # Menu
        mnu_barra = tk.Menu(self.janela)  # Barra
        mnu_arquivo = tk.Menu(mnu_barra, tearoff=0)  # Item
        mnu_barra.add_cascade(label='Arquivo', menu=mnu_arquivo)
        mnu_arquivo.add_command(label='Novo Arquivo...')  # Sub itens
        mnu_arquivo.add_command(label='Sair', command=self.janela.destroy)
        self.janela.config(menu=mnu_barra)

        mnu_editar = tk.Menu(mnu_barra, tearoff=0)
        mnu_barra.add_cascade(label='Editar', menu=mnu_editar)
        mnu_editar.add_command(label='Copiar')
        mnu_editar.add_command(label='Colar')
        mnu_editar.add_command(label='Recortar')
        mnu_editar.add_separator()

        mnu_pesquisar = tk.Menu(mnu_editar, tearoff=0)  # Tearoff Tira aquela linha chata
        mnu_editar.add_cascade(label='Pesquisar', menu=mnu_pesquisar)
        mnu_pesquisar.add_command(label='Arquivo')
        mnu_pesquisar.add_command(label='Caracter')
        mnu_pesquisar.add_command(label='Palavra')

        # Barra de rolagem
        scb_texto = tk.Scrollbar(self.janela)
        scb_texto.pack(side=tk.RIGHT, fill=tk.Y)
        # Caixa de Texto
        txt_obs = tk.Text(self.janela, height=5, width=50, yscrollcommand=scb_texto.set)
        txt_obs.pack(side=tk.LEFT, fill=tk.BOTH)
        scb_texto.config(command=txt_obs.yview)
        # Caixa de texto com a barra automática
        txt_auto = ScrolledText(self.janela)
        txt_auto.pack()


app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()
