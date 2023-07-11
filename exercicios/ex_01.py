import tkinter as tk
import datetime


class Tela:

    def conteudos(self):
        lbl_confirmacao = tk.Label(self.janela, text='Os conteudos selecionados irão ser enviados ao seu email!')
        lbl_confirmacao.pack()

    def confirmar(self):
        # Essa parte aqui é para fazer o calcúlo da idade da pessoa, não fiz nenhuma confirmação de entrada de data
        # somente para não alongar muito o codigo.
        lbl_print = tk.Label(self.janela)
        idade = self.data.get()
        ano_atual = datetime.datetime.now().year
        calcular_idade = ano_atual - int(idade)
        # Exibir valor na Label
        lbl_print.config(text=f'Seu nome é {self.nome.get()}, e sua idade é {calcular_idade} anos')
        lbl_print.pack()
        # Aqui a função irá identificar qual opção escolhida no radiobutton para mostrar ou não os checkbuttons
        if self.opcao.get() == 'S':
            # Checkbuttons para a segunda parte do exercicio
            lbl_selecione = tk.Label(self.janela, text='Selecione os conteudos de interesse:')
            lbl_selecione.pack()
            cbt_jogos = tk.Checkbutton(self.janela, text='Jogos')
            cbt_jogos.pack()
            cbt_programacao = tk.Checkbutton(self.janela, text='Programação')
            cbt_programacao.pack()
            cbt_atualidades = tk.Checkbutton(self.janela, text='Atualidades')
            cbt_atualidades.pack()
            cbt_inovacao = tk.Checkbutton(self.janela, text='Inovação')
            cbt_inovacao.pack()
            cbt_promocoes = tk.Checkbutton(self.janela, text='Promoções')
            cbt_promocoes.pack()
            # esse button e a função conteudo é meramente para mostrar a mensagem de confirmação da seleção de conteudo
            bnt_confirmar = tk.Button(self.janela, text='Confirmar', command=self.conteudos)
            bnt_confirmar.pack()
        else:
            lbl_mensagem = tk.Label(self.janela, text='Você optou por não receber nenhum conteudo em seu email!')
            lbl_mensagem.pack()

    def __init__(self, mestre):
        self.janela = mestre
        self.janela.title('Exercicio 01')
        # Variaveis para guardar o valor das entrys
        self.nome = tk.StringVar()
        self.data = tk.StringVar()
        self.opcao = tk.StringVar()
        self.opcao.set('S')

        # Entrys para a primeira parte do exercicio

        lbl_nome = tk.Label(self.janela, text='Informe seu nome:')
        lbl_nome.pack()
        ent_nome = tk.Entry(self.janela, width=40, textvariable=self.nome)
        ent_nome.pack()

        lbl_nascimento = tk.Label(self.janela, text='Informe ano de nascimento:')
        lbl_nascimento.pack()
        ent_nascimento = tk.Entry(self.janela, width=40, textvariable=self.data)
        ent_nascimento.pack()

        # Radio Button para a segunda parte do exercicio

        lbl_aceitas = tk.Label(self.janela, text='Aceita receber conteudos no seu email?')
        lbl_aceitas.pack()
        rbt_sim = tk.Radiobutton(self.janela, text='Sim', value='S', variable=self.opcao)
        rbt_sim.pack()
        rbt_nao = tk.Radiobutton(self.janela, text='Não', value='N', variable=self.opcao)
        rbt_nao.pack()

        bnt_confirmar = tk.Button(self.janela, text='Confirmar', command=self.confirmar)
        bnt_confirmar.pack()


master = tk.Tk()
app = Tela(master)
master.mainloop()

# Outra forma de fazer
"""
import tkinter as tk
from datetime import datetime


# Mensagem para confirmar a seleção de conteudo do e-mail
def confirma():
    lbl_conf = tk.Label(janela, text='Os conteudos selecionados serão enviados para o seu email!')
    lbl_conf.pack()


# Função para mostrar a idade e ipedir o usuario de não preencher as entrys
def idade():
    if nome.get() == '' or ano.get().isnumeric() is False:
        lbl_res.config(text='Os dados não foram preenchidos corretamente, tente novamente!')
    else:
        atual = datetime.now().year
        lbl_res.config(text=f'Olá, {nome.get()}! sua idade é {atual - int(ano.get())}.')
        if opcao.get() == 1:
            lbl_pref.config(text='Você optou por não receber nenhum conteudo.')
        else:
            lbl_pref.config(text='Selecione os conteudos que deseja receber:')
            cbt1 = tk.Checkbutton(janela, text='Noticias')
            cbt1.pack()
            cbt2 = tk.Checkbutton(janela, text='Jogos')
            cbt2.pack()
            cbt3 = tk.Checkbutton(janela, text='Lançamentos')
            cbt3.pack()
            cbt4 = tk.Checkbutton(janela, text='Dicas')
            cbt4.pack()
            btn2 = tk.Button(janela, text='Ok', command=confirma)
            btn2.pack()


# Parametros da janela e variaveis
janela = tk.Tk()
janela.geometry('400x500')
nome = tk.StringVar()
ano = tk.StringVar()
opcao = tk.IntVar()
opcao.set(0)

# Entrada do nome
nome_lbl = tk.Label(janela, text='Nome:')
nome_lbl.pack()
nome_entry = tk.Entry(janela, width=30, textvariable=nome)
nome_entry.pack()

# Entrada do ano de nascimento
ano_lbl = tk.Label(janela, text='Ano de Nascimento:')
ano_lbl.pack()
ano_entry = tk.Entry(janela, width=30, textvariable=ano)
ano_entry.pack()

# Preferencias do cadastro
conteudo_lbl = tk.Label(janela, text='Deseja receber conteudos no seu e-mail?')
conteudo_lbl.pack()
rbt1 = tk.Radiobutton(janela, text='Sim', variable=opcao, value=0)
rbt1.pack()
rbt2 = tk.Radiobutton(janela, text='Não', variable=opcao, value=1)
rbt2.pack()

# Botão para confirmar as entradas
btn1 = tk.Button(janela, text='Confirmar', command=idade)
btn1.pack()
lbl_res = tk.Label(janela, text='')
lbl_res.pack()
lbl_pref = tk.Label(janela, text='')
lbl_pref.pack()

janela.mainloop()
"""
