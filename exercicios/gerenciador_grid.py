import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Gerenciador Grid')
        self.janela.geometry('200x100')
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Widgets dos botões formando a piramide
        btn1 = tk.Button(self.frame, text='1', padx=10, pady=4)
        btn1.grid(row=0, column=2)
        btn2 = tk.Button(self.frame, text='2', padx=10, pady=4)
        btn2.grid(row=1, column=1, columnspan=2)  # O columnspan aqui faz esses dois botões ficarem no meio
        btn3 = tk.Button(self.frame, text='3', padx=10, pady=4)
        btn3.grid(row=1, column=2, columnspan=2)
        btn4 = tk.Button(self.frame, text='4', padx=10, pady=4)
        btn4.grid(row=2, column=1)
        btn5 = tk.Button(self.frame, text='5', padx=10, pady=4)
        btn5.grid(row=2, column=2)
        btn6 = tk.Button(self.frame, text='6', padx=10, pady=4)
        btn6.grid(row=2, column=3)
        """
        # Centralizando os botões na tela, não acho que isso seja realmente necessario, coloquei só para ficar igual.
        # self.janela.grid_rowconfigure()
        self.janela.grid_columnconfigure(0, weight=1)  # em suma, ele pega a linha que ficou vazia e conta como espaço.
        self.janela.grid_columnconfigure(4, weight=1)
        """


master = tk.Tk()
app = Tela(master)
master.mainloop()
