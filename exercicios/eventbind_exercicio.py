# By: Adrias Soares de Souza™| Matricula: 20180300017
# Finalizado: 10/07/2023 às 23:11
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class Tela:
    def __init__(self, janela):
        self.janela = janela
        # Label Frame
        lfr = tk.LabelFrame(self.janela)
        lfr.pack()

        # Botões
        self.btn1 = tk.Button(lfr, text='Pressione qualquer tecla')
        self.btn1.grid(row=0, column=0)
        btn2 = tk.Button(lfr, text='Limpar Tela', command=self.limpar_tela)
        btn2.grid(row=3, column=0)

        # Caixa de texto com scrollbar (ScrollText)
        # Obs: state=tk.DISABLED é para deixar em modo leitura e impedir que o CORNO do usuario altere o que ta na SCB
        self.scb_texto = ScrolledText(lfr, width=50, state=tk.DISABLED)
        self.scb_texto.grid(row=1, column=0)

        # comando bind associado a janela
        self.janela.bind("<KeyPress>", self.clique)
        self.btn1.bind("<KeyPress>", self.clique)

    def clique(self, evento):
        # Fiz essa lista com todos os caracteres epeciais por ser o unico jeito que consegui fazeer isso funcionar
        especiais = ["F", "KP", "Shift", "Control", "Alt", "Delete", "Insert", "Home", "End", "Page_Up", "Page_Down",
                     "Left", "Right", "Up", "Down", "Num_Lock", "Scroll_Lock", "Print", "Prior", "Clear", "Next", "Tab",
                     "Caps_Lock", "Win_L", "Space", "Return", "BackSpace", "Escape"]

        # Verifica se é uma tecla "normal" (Alfanumerico), ou de pontuação
        if evento.char.isalnum():
            tipo = "Tecla Normal"
        else:
            tipo = "Tecla de Pontuação"

        # Vai verificar se a tecla precionada se encaixa na categoria especial e sobrescreve o tipo para especial
        for especial in especiais:
            if especial in evento.keysym:
                tipo = "Tecla Especial"
                break

        # Meramente para mostrar com o adicional da parte "Tecla" se for uma tecla de pontuação
        if tipo == "Tecla de Pontuação":
            self.scb_texto.config(state=tk.NORMAL)
            self.scb_texto.insert(tk.END, f"{tipo}: {evento.keysym} Tecla: {evento.char}\n")
            self.scb_texto.config(state=tk.DISABLED)
        else:
            self.scb_texto.config(state=tk.NORMAL)
            self.scb_texto.insert(tk.END, f"{tipo}: {evento.keysym}\n")
            self.scb_texto.config(state=tk.DISABLED)

        # Rolar para a automaticamente para a última linha conforme for atualizado a SCB
        self.scb_texto.see(tk.END)

        # OBS: Por algum KRL de razão algumas teclas como ^, ~, ¨ só aparecem após clicar 2x na tecla

    # Função para limpar a TextScrollbar
    def limpar_tela(self):
        self.scb_texto.config(state=tk.NORMAL)
        self.scb_texto.delete("1.0", tk.END)
        self.scb_texto.config(state=tk.DISABLED)


# Gera a janela, passa ela para ser trabalhada na classe e mantem a tela rodando, nessa ordem
main = tk.Tk()
app = Tela(main)
main.mainloop()
