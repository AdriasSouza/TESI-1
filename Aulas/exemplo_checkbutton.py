import tkinter as tk


class Tela:
    def mostrar(self):
        lbl_mostrar = tk.Label(self.janela)
        lbl_mostrar['text'] = f'{self.basico.get()} {self.avancado.get()}'
        # lbl_mostrar.config(text=self.basico.get())
        lbl_mostrar.pack()

    def __init__(self, master):
        self.janela = master  # Master agora tem o nome de self.janela
        self.janela.title('Exemplo Chackbutton')
        self.janela.geometry('300x500')
        self.basico = tk.IntVar()
        self.avancado = tk.IntVar()
        cbt_basico = tk.Checkbutton(self.janela,
                                    text='Básico',
                                    variable=self.basico,
                                    command=self.mostrar)  # O pai dela é esse
        # selectcolor='black')
        cbt_basico.pack()
        cbt_avancado = tk.Checkbutton(self.janela,
                                      text='Avançado',
                                      variable=self.avancado,
                                      command=self.mostrar)
        # selectcolor='black')
        cbt_avancado.pack()
        print(self.basico)
        print(self.avancado)


master = tk.Tk()
app = Tela(master)  # Esse recurso vai ser customizado dentro da janela
master.mainloop()  # Mantem a janela em execução
