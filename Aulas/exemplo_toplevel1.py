import tkinter as tk


def abrir_janela():
    """Janela Top level"""
    top = tk.Toplevel()
    top.geometry("200x200")
    top.title("Janela Toplevel")
    # Label da Top Level
    lbl3 = tk.Label(top, text="Está é uma janela Toplevel")
    lbl3.pack()
    # Botão para fechar a janela
    btn2 = tk.Button(top, text='Fechar', command=top.destroy)
    btn2.pack()


"""Janela Principal"""
janela = tk.Tk()
janela.geometry("300x300")
janela.title("Janela Principal da Aplicação")

# Label da janela principal
lbl1 = tk.Label(janela, text="Esta é a janela principal da aplicação.")
lbl1.pack()

# Botão para chamar a Top Level
lbl2 = tk.Label(janela, text="Clique no botão abaixo para mostrar a TopLevel:")
lbl2.pack()
btn1 = tk.Button(janela, text="Nova Janela", command=abrir_janela)
btn1.pack()

janela.mainloop()
