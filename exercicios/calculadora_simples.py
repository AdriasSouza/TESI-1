import tkinter as tk


class Tela:

    def imprimir(self):
        pass

    def __init__(self, master):
        self.janela = master
        self.janela.title('Calculadora Simples')
        self.janela.geometry('280x430')
        self.frame = tk.Frame(self.janela)
        self.frame.pack()
        self.valor = tk.StringVar()
        self.valor.set('0')

        # O entry representando a tela da calculadora, onde os números são apresentados
        tela_entry = tk.Entry(self.frame, width=40, relief=tk.SUNKEN, border=10, textvariable=self.valor)  # relief é o
        # formato da borda
        tela_entry.grid(row=0, columnspan=4, padx=10, pady=10)

        # Botões:
        # Fileira 1
        btn_7 = tk.Button(self.frame, text='7', padx=20, pady=22, relief=tk.RAISED, border=5, command=self.imprimir)
        btn_7.grid(row=1, column=0)
        btn_8 = tk.Button(self.frame, text='8', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_8.grid(row=1, column=1)
        btn_9 = tk.Button(self.frame, text='9', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_9.grid(row=1, column=2)
        btn_som = tk.Button(self.frame, text='+', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_som.grid(row=1, column=3)

        # Fileira 2
        btn_4 = tk.Button(self.frame, text='4', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_4.grid(row=2, column=0)
        btn_5 = tk.Button(self.frame, text='5', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_5.grid(row=2, column=1)
        btn_6 = tk.Button(self.frame, text='6', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_6.grid(row=2, column=2)
        btn_sub = tk.Button(self.frame, text='-', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_sub.grid(row=2, column=3)

        # Fileira 3
        btn_1 = tk.Button(self.frame, text='1', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_1.grid(row=3, column=0)
        btn_2 = tk.Button(self.frame, text='2', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_2.grid(row=3, column=1)
        btn_3 = tk.Button(self.frame, text='3', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_3.grid(row=3, column=2)
        btn_mult = tk.Button(self.frame, text='*', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_mult.grid(row=3, column=3)

        # Fileira 4
        btn_0 = tk.Button(self.frame, text='0', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_0.grid(row=4, column=0)
        btn_dot = tk.Button(self.frame, text='.', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_dot.grid(row=4, column=1)
        btn_c = tk.Button(self.frame, text='C', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_c.grid(row=4, column=2)
        btn_div = tk.Button(self.frame, text='/', padx=20, pady=22, relief=tk.RAISED, border=5)
        btn_div.grid(row=4, column=3)

        # Fileira 5
        btn_res = tk.Button(self.frame, text='=', padx=120, pady=22, relief=tk.RAISED, border=5, bg='green', font=(
            'Arial', 18), fg='white')
        btn_res.grid(row=5, column=0, columnspan=4)


master = tk.Tk()
app = Tela(master)
master.mainloop()
