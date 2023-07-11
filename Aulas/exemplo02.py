import tkinter as tk  # isso


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Primeira Janela')
        self.janela.geometry('500x500')
        # janela.minsize(200, 400)
        # janela.maxsize(800, 600)
        master.resizable(width=False, height=False)  # pro usuario não mecher no tamanho da janela
        container1 = tk.Frame(self.janela, width=500, height=250, bg='red', borderwidth=10, relief=tk.RAISED)
        container1.pack()
        container2 = tk.Frame(self.janela, width=500, height=250, bg='blue', borderwidth=5, relief=tk.SUNKEN)
        container2.pack()

master = tk.Tk()
tela = Tela(master)
master.mainloop()
