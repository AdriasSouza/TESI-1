import tkinter as tk
from PIL import Image, ImageTk  # Pillow

janela = tk.Tk()

caminho_imagem = Image.open('capivara.jpg')
imagem = caminho_imagem.resize((200, 150))
imagem = ImageTk.PhotoImage(imagem)

lbl = tk.Label(janela, image=imagem)
lbl.pack()

janela.mainloop()
