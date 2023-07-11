import tkinter as tk

janela = tk.Tk()

lbl_user = tk.Label(janela, text='USUARIO')
lbl_user.grid(row=0, column=0)
lbl_pass = tk.Label(janela, text='SENHA')
lbl_pass.grid(row=0, column=1)
ent_user = tk.Entry(janela)
ent_user.grid(row=1, column=1)
ent_pass = tk.Entry(janela)
ent_pass.grid(row=1, column=0)
btn = tk.Button(janela, text='ENTRAR')
btn.grid(row=2, column=0, columnspan=2)


janela.mainloop()
