import tkinter as tk

janela = tk.Tk()
janela.geometry('320x200')
janela.title('LabelFrame')

lfr = tk.LabelFrame(janela, text='Alinhamento', labelanchor=tk.N)
lfr.grid(column=0, row=0, padx=20, pady=20)

var = tk.StringVar()
var.set('L')

rbt1 = tk.Radiobutton(lfr, text='LEFT', value='L', variable=var)
rbt1.grid(column=0, row=0, ipadx=10, ipady=10)
rbt2 = tk.Radiobutton(lfr, text='CENTER', value='C', variable=var)
rbt2.grid(column=1, row=0, ipadx=10, ipady=10)
rbt3 = tk.Radiobutton(lfr, text='RIGHT', value='R', variable=var)
rbt3.grid(column=2, row=0, ipadx=10, ipady=10)

janela.mainloop()
