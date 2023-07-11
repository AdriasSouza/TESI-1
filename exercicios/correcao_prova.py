import tkinter as tk


class Tela:

    def fechar(self):
        self.janela.destroy()

    def mostrar(self):
        if self.opcao.get():
            self.lbl_res.config(text=f'{self.nome.get()}')
        else:
            self.lbl_res.config(text=f'{self.nome.get().lower()}')

    def __init__(self, master):
        self.janela = master
        self.nome = tk.StringVar()
        self.opcao = tk.IntVar()
        self.janela.title('Localizar e substituir')

        # Labels e Entrys da janela
        lbl1 = tk.Label(self.janela, text='Localizar:')
        lbl1.grid(row=0, column=0)
        ent1 = tk.Entry(self.janela, textvariable=self.nome)
        ent1.grid(row=0, column=1, sticky='we', columnspan=2)
        lbl2 = tk.Label(self.janela, text='Substituir:')
        lbl2.grid(row=1, column=0)
        ent2 = tk.Entry(self.janela)
        ent2.grid(row=1, column=1, sticky='we', columnspan=2)

        # Label Frames
        lbf1 = tk.LabelFrame(self.janela, text='Opções')
        lbf1.grid(row=2, column=1, rowspan=3)
        cbt1 = tk.Checkbutton(lbf1, text='Corresponder palavra inteira')
        cbt1.grid(row=0, column=0, sticky='w')
        cbt2 = tk.Checkbutton(lbf1, text='Considerar letras maiúsculas e minúsculas', variable=self.opcao)
        cbt2.grid(row=1, column=0, sticky='w')
        cbt3 = tk.Checkbutton(lbf1, text='Diferenciar Maiusculas e Minusculas')
        cbt3.grid(row=2, column=0, sticky='w')
        lbf2 = tk.LabelFrame(self.janela, text='Direção')
        lbf2.grid(row=2, column=2, rowspan=3)
        rbt1 = tk.Radiobutton(lbf2, text='Acima')
        rbt1.pack()
        rbt2 = tk.Radiobutton(lbf2, text='Abaixo')
        rbt2.pack()

        # Botões
        btn1 = tk.Button(janela, text='Localizar Proximo', command=self.mostrar)
        btn1.grid(row=0, column=3, sticky='we')
        btn2 = tk.Button(janela, text='Localizar Tudo')
        btn2.grid(row=1, column=3, sticky='we')
        btn3 = tk.Button(janela, text='Substituir')
        btn3.grid(row=2, column=3, sticky='we')
        btn4 = tk.Button(janela, text='Substituir Tudo')
        btn4.grid(row=3, column=3, sticky='we')
        btn5 = tk.Button(janela, text='Fechar', command=self.fechar)
        btn5.grid(row=4, column=3, sticky='we')

        # Label vazia para mostrar a interação com proximo
        self.lbl_res = tk.Label(janela, text='', bg='white', padx=60)
        self.lbl_res.grid(row=5, column=1, columnspan=2)


janela = tk.Tk()
app = Tela(janela)
janela.mainloop()
