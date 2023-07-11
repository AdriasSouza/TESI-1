import tkinter as tk

janela = tk.Tk()

frame1 = tk.Frame(janela, bg='green', width=200)  # são containers que servem para adicionar outros componentes
frame1.pack(side=tk.TOP)
btn1 = tk.Button(frame1, text='1')
btn1.grid(row=0, column=1)
btn2 = tk.Button(frame1, text='2')
btn2.grid(row=0, column=2)
btn3 = tk.Button(frame1, text='3')
btn3.grid(row=1, column=1, columnspan=2)

frame2 = tk.LabelFrame(janela, text='Titulo do frame', labelanchor=tk.N, bg='blue', height=200, width=200)  # obrigatoriamente tem que informar o ancestral deles
frame2.pack()
btn4 = tk.Button(frame2, text='Botão 4')
btn4.grid(row=0, column=1)
btn5 = tk.Button(frame2, text='Botão 5')
btn5.grid(row=0, column=2)
btn6 = tk.Button(frame2, text='Botão 6')
btn6.grid(row=1, column=1, columnspan=2)



janela.mainloop()
