import tkinter as tk

janela = tk.Tk()

janela.title('Pack simples')
janela.geometry('300x200')
# Topo e fundo
lbl1 = tk.Label(janela, text='TOPO', bg='yellow')
lbl1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
lbl4 = tk.Label(janela, text='RODAPÉ', bg='cyan')
lbl4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
# Lados esquerdo e direito
lbl2 = tk.Label(janela, text='ESQUERDA', bg='red')
lbl2.pack(side=tk.LEFT, fill=tk.X, expand=True)
lbl3 = tk.Label(janela, text='DIREITA', bg='green')
lbl3.pack(side=tk.RIGHT, fill=tk.X, expand=True)


janela.mainloop()
