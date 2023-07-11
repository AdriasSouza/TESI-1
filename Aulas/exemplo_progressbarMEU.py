"""importações"""
import threading
import tkinter as tk
from tkinter import ttk

"""Parametros da Janela"""
janela = tk.Tk()
janela.title('Progressbar')
v = tk.IntVar()
# variavel de controle para a label contadora
parou = 0

"""Funções da Janela"""


def thread():
    global parou
    # "Parou" aqui recebe 0 para que em caso de o programa ser pausado, ele possa voltar a executar a label de progresso
    parou = 0
    # Faz com que o que for executado por "iniciar" possa rodar em paralelo com outras atividades
    th = threading.Thread(target=iniciar)
    th.start()


# Inicia a progressbar e a função "mostrar" para atualizar a label de progresso
def iniciar():
    prb.start()
    mostrar()


def mostrar():
    # Ele faz a verificação através do proprio valor do prb, e para a execução quando chegar em 100%
    if prb['value'] < 101:
        # Para a contagem caso o botão de "Stop" seja acionado
        if parou == 1:
            return
        print(prb['value'])
        lbl.config(text=f"{int(prb['value'])}%")
        # Recursividade para chamar a função mostrar a cada 50ms e atualizar a label
        lbl.after(50, mostrar)
    else:
        parar()


# Para a prb e a label
def parar():
    global parou
    parou = 1
    prb.stop()


# Chama a função parar e redefine os valores para zero
def reiniciar():
    parar()
    v.set(0)
    lbl.config(text='0%')


"""Elementos da janela"""
# Barra de Progresso
prb = ttk.Progressbar(janela, mode='determinate', variable=v, maximum=102, length=200)
prb.grid(row=0, column=0, columnspan=3)
# Label para mostrar a porcentagem
lbl = tk.Label(janela, text='0%')
lbl.grid(row=0, column=3)
# Botões de Iniciar, Parar e Reiniciar
btn_start = tk.Button(janela, text='Start', command=thread)
btn_start.grid(row=1, column=0)
btn_stop = tk.Button(janela, text='Stop', command=parar)
btn_stop.grid(row=1, column=1)
btn_restart = tk.Button(janela, text='Restart', command=reiniciar)
btn_restart.grid(row=1, column=2)

"""Mantem a janela rodando"""
janela.mainloop()
