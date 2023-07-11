import tkinter as tk

janela = tk.Tk()

lbl1 = tk.Label(janela, text='LEFT1', bg='brown')
lbl1.pack(padx=20, ipadx=10, fill=tk.Y, expand=True, side=tk.LEFT)
lbl2 = tk.Label(janela, text='LEFT2', bg='green')
lbl2.pack(padx=20, ipadx=10, side=tk.LEFT)
lbl3 = tk.Label(janela, text='RIGHT1', bg='blue')
lbl3.pack(padx=20, ipadx=10, fill=tk.X, expand=True, side=tk.RIGHT)
lbl4 = tk.Label(janela, text='RIGHT2', bg='yellow')
lbl4.pack(padx=20, ipadx=10, side=tk.RIGHT)

janela.mainloop()
