import tkinter as tk

janela = tk.Tk()


# Event bind
def keypress(evento):
    lbl.config(text=f'Keypress:{evento.keysym}')


def keyrelease(e):
    lbl.config(text='KeyRelease')


lbl = tk.Label(janela, text='')
lbl.pack()
janela.bind('<KeyPress>', keypress)
janela.bind('<KeyRelease>', keyrelease, add='+')

janela.mainloop()
