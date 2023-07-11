import tkinter as tk

# Inicia a Janela e parametros
janela = tk.Tk()
janela.geometry('300x300')
janela.title('Gerenciador Pack')

# Esses 3 primeiros são para definir as 3 primeiras cores do topo
lbl1 = tk.Label(text='Red', bg='red')
lbl1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
lbl2 = tk.Label(text='Green', bg='green')
lbl2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
lbl3 = tk.Label(text='Blue', bg='blue')
lbl3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# Logo após a label azul, coloquei as duas cinzas nos lados, elas estão com a numeração maior por serem as ultímas
# que coloquei.
lbl8 = tk.Label(text='Gray', bg='gray')
lbl8.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
lbl9 = tk.Label(text='Gray', bg='gray')
lbl9.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Label preta ocupando o rodapé da pagína, ela não ficou do mesmo tamanho que o exemplo :/
# Ps: Acredito que consegui
lbl4 = tk.Label(text='Black', bg='black', fg='White', pady=50)
lbl4.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

# As labels que ficam no meio, porque elas ficam no meio? Eu não faço ideia, só sei que funcionou assim nessa ordem.
# Ps 2: acredito que pela label 'black' já estar no fundo, eles são jogados para cima dele, e como já tinha duas cinzas
# ocupando o espaço da esquerda e direita, ele posiciona-as entre essas duas que tem prioridade, e abaixo das de cima.
lbl5 = tk.Label(text='Cyan', bg='cyan')
lbl5.pack(side=tk.LEFT, expand=True, fill=tk.X)
lbl6 = tk.Label(text='Magenta', bg='magenta')
lbl6.pack(side=tk.LEFT, expand=True, fill=tk.X)
lbl7 = tk.Label(text='Yellow', bg='yellow')
lbl7.pack(side=tk.RIGHT, expand=True, fill=tk.X)

janela.mainloop()

# Outra forma de fazer
"""
import tkinter as tk

# Parametros e variaveis da janela
janela = tk.Tk()
janela.title('Gerenciador Pack')
janela.geometry('300x300')

# Labels
lbl1 = tk.Label(janela, text='Red', bg='red', fg='white', pady=10)
lbl1.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
lbl2 = tk.Label(janela, text='Green', bg='green', fg='white', pady=10)
lbl2.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
lbl3 = tk.Label(janela, text='Blue', bg='blue', fg='white', pady=10)
lbl3.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
lbl4 = tk.Label(janela, text='Gray', bg='gray')
lbl4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lbl5 = tk.Label(janela, text='Gray', bg='gray')
lbl5.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
lbl6 = tk.Label(janela, text='Black', bg='black', fg='white')
lbl6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
lbl7 = tk.Label(janela, text='Cyan', bg='cyan', pady=10)
lbl7.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lbl8 = tk.Label(janela, text='Magenta', bg='magenta', pady=10)
lbl8.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lbl9 = tk.Label(janela, text='Yellow', bg='yellow', pady=10)
lbl9.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


janela.mainloop()

"""
