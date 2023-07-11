import tkinter as tk

janela = tk.Tk()


# Event bind
def clicou(evento):
    lbl = tk.Label(janela, text='Não pressionou Caps_Lock')
    lbl.pack()
    print(evento)


def log(e):
    print(e)


def teste(t):
    print('teste')


btn = tk.Button(janela, text='Clique')
btn.bind('<Any-KeyPress>', clicou)
btn.bind('<Caps_Lock>', log, add='+')  # associar o mesmo comando executa só o ultimo
# btn.bind('<a>', teste, add='+')
# Control_R
# Return
# Control-v
btn.pack()

janela.mainloop()
