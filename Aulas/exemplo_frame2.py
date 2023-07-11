import tkinter as tk

janela = tk.Tk()
janela.geometry('300x150')
janela.title('Frames')

# Frame 1
frameH = tk.Frame(janela)
frameH.pack()
btn1 = tk.Button(frameH, text="Adicionar")
btn1.pack(side=tk.RIGHT)
btn2 = tk.Button(frameH, text="Editar")
btn2.pack(side=tk.RIGHT)
btn3 = tk.Button(frameH, text="Remover")
btn3.pack(side=tk.RIGHT)

# Frame 2
frameV = tk.Frame(janela)
frameV.pack()
btn4 = tk.Button(frameV, text="Salvar")
btn4.pack(side=tk.BOTTOM)
btn5 = tk.Button(frameV, text="Fechar")
btn5.pack(side=tk.BOTTOM)
btn6 = tk.Button(frameV, text="Listar")
btn6.pack(side=tk.BOTTOM)

janela.mainloop()
