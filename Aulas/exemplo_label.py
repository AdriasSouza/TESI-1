import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master  # Master agora tem o nome de self.janela
        self.janela.title('Terceira Janela')
        self.janela.geometry('300x500')
        lbl_primeira = tk.Label(self.janela, text='Primeira Label',
                                width=50,
                                height=3,
                                padx=100,
                                pady=50,
                                relief=tk.SUNKEN,
                                bg='blue',
                                fg='yellow',
                                font='Ubuntu')
        lbl_primeira.pack()


master = tk.Tk()
app = Tela(master)  # Esse recurso vai ser customizado dentro da janela
master.mainloop()  # Mantem a janela em execução
