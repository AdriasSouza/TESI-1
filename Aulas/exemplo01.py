import tkinter as tk  # isso

janela = tk.Tk()  # é
janela.title('Primeira Janela')
janela.geometry('500x500')
# janela.minsize(200, 400)
# janela.maxsize(800, 600)
janela.resizable(width=False, height=False)  # pro usuario não mecher no tamanho da janela

container1 = tk.Frame(janela, width=500, height=250, bg='red', borderwidth=10, relief=tk.RAISED)
container1.pack()
container2 = tk.Frame(janela, width=500, height=250, bg='blue', borderwidth=5, relief=tk.SUNKEN)
container2.pack()

janela.mainloop()  # Obrigatorio
