import tkinter as tk


class Tela:
    def abrir_top(self):
        self.janela.iconify()  # iconify minimiza a janela em icone, withdraw() esconde ela completamente
        self.top = tk.Toplevel(self.janela)
        self.top.title('Janela Toplevel')
        self.top.grab_set()  # impede a interação com self.janela, se não tiver, voce pode voltar na principal e
        # abrir outra janela
        self.btn2 = tk.Button(self.top, text='Fechar', command=self.fechar_top)
        self.btn2.pack()

    def fechar_top(self):
        self.top.destroy()
        self.janela.deiconify()

    def __init__(self, master):
        self.janela = master  # "master é a variavel que recebe "App", self.janela recebe master e agora representa-a"
        self.janela.title('Janela Principal')
        self.btn1 = tk.Button(self.janela, text='Abrir', command=self.abrir_top)
        self.btn1.pack()
        self.top = None
        self.btn2 = None


app = tk.Tk()  # "App" recebe o modulo tk puxando a função Tk() que cria uma janela
Tela(app)  # Class tela recebe como parametro a variavel de janela "App"
app.mainloop()  # Mantem a janela aberta
