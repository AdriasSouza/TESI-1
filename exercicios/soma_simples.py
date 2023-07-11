import tkinter as tk


# Função soma para efetuar o calcúlo dos números
def soma():
    s = num1.get() + num2.get()
    lbl_res.config(text=f'{s}')  # essa linha atualiza a label do resultado sempre que a função soma é chamada.


# Inicia a janela e parametros
janela = tk.Tk()
janela.geometry('240x80')
janela.title('Soma Simples')
num1 = tk.DoubleVar()
num2 = tk.DoubleVar()

# Primeira label e entry, onde é inserido o primeiro número.
lbl1 = tk.Label(janela, text='Número 1:')
lbl1.grid(row=0, column=0)
ent1 = tk.Entry(janela, textvariable=num1)
ent1.grid(row=0, column=1)

# Segunda label e entry, onde é inserido o segundo número.
lbl2 = tk.Label(janela, text='Número 2:')
lbl2.grid(row=1, column=0)
ent2 = tk.Entry(janela, textvariable=num2)
ent2.grid(row=1, column=1)

# Botão "Somar" que chama a função soma para efetuar o calcúlo.
btn_soma = tk.Button(janela, text='Somar >>', padx=5, command=soma)
btn_soma.grid(row=2, column=0, padx=10)

# Label onde o resultado é exibido
lbl_res = tk.Label(janela, text='0.0', bg='white', width=15)
lbl_res.grid(row=2, column=1)

janela.mainloop()

# Outra forma
"""
import tkinter as tk

# Propriedades e variaveis da janela
janela = tk.Tk()
janela.title('Soma Simples')
janela.geometry('200x100')
num1 = tk.StringVar()
num2 = tk.StringVar()


# Funcao Somar
def somar():
    if not num1.get().replace('.', '', 1).isdigit() or not num2.get().replace('.', '', 1).isdigit():
        lbl3.config(text='ERRO')
    else:
        lbl3.config(text=f'{float(num1.get()) + float(num2.get())}')


# Elementos da interface
lbl1 = tk.Label(janela, text='Número 1:')
lbl1.grid(row=0, column=0)
ent1 = tk.Entry(janela, width=20, textvariable=num1)
ent1.grid(row=0, column=1)
lbl2 = tk.Label(janela, text='Número 2:')
lbl2.grid(row=1, column=0)
ent2 = tk.Entry(janela, width=20, textvariable=num2)
ent2.grid(row=1, column=1)
btn1 = tk.Button(janela, text='Somar >>', command=somar)
btn1.grid(row=2, column=0)
lbl3 = tk.Label(janela, text='', bg='white', width=10)
lbl3.grid(row=2, column=1)

janela.mainloop()
"""
