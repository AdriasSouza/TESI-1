import tkinter as tk


class Tela:
    def __init__(self, master):
        self.janela = master
        self.imagem = tk.PhotoImage(file='Logo-ufac.png')
        imagem_red = self.imagem.subsample(2, 2)  # Redimensiona a imagem
        lbl = tk.Label(self.janela, image=self.imagem)
        lbl.pack()


mestre = tk.Tk()
app = Tela(mestre)
mestre.mainloop()
