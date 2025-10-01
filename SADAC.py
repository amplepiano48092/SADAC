import customtkinter as ctk
from pygame import mixer
from PIL import Image
import os
print(os.path.exists("MapaArboreio.jpeg"))

# Inicializa o mixer do Pygame
ctk.set_appearance_mode('dark')
mixer.init()

# Criando a interface
arboreio = ctk.CTk()
arboreio.title('Arboreio')
arboreio.geometry('450x650')

# Função para fechar a janela principal
def fechar():
    arboreio.destroy()

# Função para a aba Mapa Sadac
def mapasadc():
    mapa_sadac = ctk.CTk()
    mapa_sadac.title('Mapa Sadac')
    mapa_sadac.geometry('450x650')

    # Armazenar a referência à imagem globalmente para evitar garbage collection
    mapa_sadac.imagem_ref = None  # Criar uma referência na janela

    # Carregar a imagem MapaArboreio.jpeg
    caminho_imagem = r"alex\MapaArboreio.jpg"  # Ajuste o caminho se necessário
    if os.path.exists(caminho_imagem):
        try:
            # Carregar a imagem com CTkImage
            mapa_sadac.imagem_ref = ctk.CTkImage(
                light_image=Image.open(r'alex\MapaArboreio.jpg'),
                dark_image=Image.open(r'alex\MapaArboreio.jpg'),
                size=(450, 650)  # Ajustado para caber na janela
            )
            # Criar um label com a imagem
            label_imagem = ctk.CTkLabel(master=mapa_sadac, image=mapa_sadac.imagem_ref, text="")
            label_imagem.place(relx=0, rely=0, relwidth=1, relheight=1)  # Imagem como fundo
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            erro_label = ctk.CTkLabel(master=mapa_sadac, text=f"Erro: Não foi possível carregar a imagem\n{e}", font=('Times New Roman', 14))
            erro_label.place(relx=0.5, rely=0.5, anchor="center")
    else:
        print(f"Arquivo {caminho_imagem} não encontrado.")
        erro_label = ctk.CTkLabel(master=mapa_sadac, text=f"Erro: Arquivo {caminho_imagem} não encontrado.", font=('Times New Roman', 14))
        erro_label.place(relx=0.5, rely=0.5, anchor="center")

    def voltar():
        mapa_sadac.destroy()

    # Funções para reproduzir música (mantidas iguais)
    def I():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\1 - Pau-brasil.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def II():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\2 - Jenipapo.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def III():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\3 - Abiu-roxo.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def IV():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\4 - Ingá-branco.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def V():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\5 - Jamelão.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def VI():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\6 - Palmeira-imperial.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def VII():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\7 - Pau-ferro.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def VIII():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\8 - Aldrago.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def IX():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\9 - Tataré.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def X():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\10 - Munguba.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def XI():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\11 - Amoreira-negra.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def XII():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\12 - Mogno-africano.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def XIII():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\13 - Jatobá.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def XIV():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\14- Ipê-rosa.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    def XV():
        try:
            if mixer.music.get_busy():
                mixer.music.stop()
            else:
                mixer.music.load(r"alex\audios\15 - Mogno-brasileiro.mp3")
                mixer.music.play()
        except Exception as e:
            print(f"Erro ao reproduzir música: {e}")

    # Seleção das árvores (botões 1 a 15)
    I = ctk.CTkButton(master=mapa_sadac, text='1', width=20, height=20, font=('Times New Roman', 12), command=I)
    II = ctk.CTkButton(master=mapa_sadac, text='2', width=20, height=20, font=('Times New Roman', 12), command=II)
    III = ctk.CTkButton(master=mapa_sadac, text='3', width=20, height=20, font=('Times New Roman', 12), command=III)
    IV = ctk.CTkButton(master=mapa_sadac, text='4', width=20, height=20, font=('Times New Roman', 12), command=IV)
    V = ctk.CTkButton(master=mapa_sadac, text='5', width=20, height=20, font=('Times New Roman', 12), command=V)
    VI = ctk.CTkButton(master=mapa_sadac, text='6', width=20, height=20, font=('Times New Roman', 12), command=VI)
    VII = ctk.CTkButton(master=mapa_sadac, text='7', width=20, height=20, font=('Times New Roman', 12), command=VII)
    VIII = ctk.CTkButton(master=mapa_sadac, text='8', width=20, height=20, font=('Times New Roman', 12), command=VIII)
    IX = ctk.CTkButton(master=mapa_sadac, text='9', width=20, height=20, font=('Times New Roman', 12), command=IX)
    X = ctk.CTkButton(master=mapa_sadac, text='10', width=20, height=20, font=('Times New Roman', 12), command=X)
    XI = ctk.CTkButton(master=mapa_sadac, text='11', width=20, height=20, font=('Times New Roman', 12), command=XI)
    XII = ctk.CTkButton(master=mapa_sadac, text='12', width=20, height=20, font=('Times New Roman', 12), command=XII)
    XIII = ctk.CTkButton(master=mapa_sadac, text='13', width=20, height=20, font=('Times New Roman', 12), command=XIII)
    XIV = ctk.CTkButton(master=mapa_sadac, text='14', width=20, height=20, font=('Times New Roman', 12), command=XIV)
    XV = ctk.CTkButton(master=mapa_sadac, text='15', width=20, height=20, font=('Times New Roman', 12), command=XV)

    # Posicionamento dos botões com place() (ajuste conforme necessário)
    I.place(relx=0.1, rely=0.1)
    II.place(relx=0.2, rely=0.1)
    III.place(relx=0.3, rely=0.1)
    IV.place(relx=0.4, rely=0.1)
    V.place(relx=0.5, rely=0.1)
    VI.place(relx=0.6, rely=0.1)
    VII.place(relx=0.7, rely=0.1)
    VIII.place(relx=0.8, rely=0.1)
    IX.place(relx=0.1, rely=0.2)
    X.place(relx=0.2, rely=0.2)
    XI.place(relx=0.3, rely=0.2)
    XII.place(relx=0.4, rely=0.2)
    XIII.place(relx=0.5, rely=0.2)
    XIV.place(relx=0.6, rely=0.2)
    XV.place(relx=0.7, rely=0.2)

    # Botão de voltar
    retroceder = ctk.CTkButton(mapa_sadac, text='←', width=40, height=20, font=('Times New Roman', 24), command=voltar)
    retroceder.place(relx=0.05, rely=0.95)  # Canto inferior esquerdo

    mapa_sadac.mainloop()

# Tela inicial
textoinicial = ctk.CTkLabel(arboreio, text='Bem vindo ao SADAC', font=('Times New Roman', 24))
textoinicial.pack(pady=10)

mapa = ctk.CTkButton(arboreio, text='Mapa', font=('Times New Roman', 24), command=mapasadc)
mapa.pack(pady=20)

sair = ctk.CTkButton(arboreio, text='Sair', font=('Times New Roman', 24), command=fechar)
sair.pack(pady=20)

arboreio.mainloop()
