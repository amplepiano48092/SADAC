import customtkinter as ctk
from pygame import mixer
from PIL import Image
import os

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
    arboreio.withdraw()
    mapa_sadac = ctk.CTkToplevel()  # Mudado para CTkToplevel em vez de CTk
    mapa_sadac.title('Mapa Sadac')
    mapa_sadac.geometry('450x650')
    
    # Criar um frame principal para organizar melhor
    principal = ctk.CTkFrame(mapa_sadac)
    principal.pack(fill="both", expand=True, padx=10, pady=10)

    # Armazenar a referência à imagem globalmente
    mapa_sadac.imagem_ref = None

    # Carregar a imagem MapaArboreio.jpeg
    caminho_imagem = r"C:\XAMPP\htdocs\alex\alex\MapaArboreio.jpeg"
    
    if os.path.exists(caminho_imagem):
        try:
            # Carregar a imagem com CTkImage
            mapa_sadac.imagem_ref = ctk.CTkImage(light_image=Image.open(caminho_imagem), dark_image=Image.open(caminho_imagem), size=(400, 282))
            
            # Criar um label com a imagem
            label_imagem = ctk.CTkLabel(master=principal, image=mapa_sadac.imagem_ref, text="")
            label_imagem.pack(pady=10)
            
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            erro_label = ctk.CTkLabel(master=principal, text=f"Erro ao carregar imagem\n{e}", font=('Times New Roman', 14))
            erro_label.pack(pady=10)
    else:
        print(f"Arquivo {caminho_imagem} não encontrado.")
        erro_label = ctk.CTkLabel(master=principal, text=f"Arquivo não encontrado: {caminho_imagem}", font=('Times New Roman', 14))
        erro_label.pack(pady=10)

    def voltar():
        arboreio.deiconify() #exibe janela
        mapa_sadac.destroy()

    # Função genérica para tocar música
    def tocar_musica(numero_arvore, nome_arquivo):
        try:
            caminho_audio = os.path.join("alex", "audio", nome_arquivo)
            if not os.path.exists(caminho_audio):
                print(f"Arquivo de áudio não encontrado: {caminho_audio}")
                return
                
            if mixer.music.get_busy():
                mixer.music.stop()
                print(f"parando: {nome_arquivo}")

            else:
                mixer.music.load(caminho_audio)
                mixer.music.play()
                print(f"Tocando: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao reproduzir música {numero_arvore}: {e}")

    # Dicionário com as músicas
    musicas = {
        1: "1 - Pau-brasil.mp3",
        2: "2 - Jenipapo.mp3", 
        3: "3 - Abiu-roxo.mp3",
        4: "4 - Ingá-branco.mp3",
        5: "5 - Jamelão.mp3",
        6: "6 - Palmeira-imperial.mp3",
        7: "7 - Pau-ferro.mp3",
        8: "8 - Aldrago.mp3",
        9: "9 - Tataré.mp3",
        10: "10 - Munguba.mp3",
        11: "11 - Amoreira-negra.mp3",
        12: "12 - Mogno-africano.mp3",
        13: "13 - Jatobá.mp3",
        14: "14- Ipê-rosa.mp3",
        15: "15 - Mogno-brasileiro.mp3"
    }

    # Frame para os botões das árvores
    frame_botoes = ctk.CTkFrame(principal)
    frame_botoes.pack(pady=10)

    # Criar botões dinamicamente
    botoes = []
    for i in range(1, 16):
        # Usar lambda com argumento padrão para capturar o valor correto
        comando = lambda num=i: tocar_musica(num, musicas[num])
        
        botao = ctk.CTkButton(master=frame_botoes, text=str(i), width=30, height=30, font=('Times New Roman', 12), command=comando)
        botoes.append(botao)

    # Organizar botões em grid
    for i, botao in enumerate(botoes):
        linha = i // 8  # 8 botões por linha
        coluna = i % 8
        botao.grid(row=linha, column=coluna, padx=2, pady=2)

    # Botão de voltar
    retroceder = ctk.CTkButton(principal, text='← Voltar',  width=80, height=30, font=('Times New Roman', 16), command=voltar)
    retroceder.pack(pady=10)

    mapa_sadac.mainloop()

# Tela inicial
frame_inicial = ctk.CTkFrame(arboreio)
frame_inicial.pack(fill="both", expand=True, padx=20, pady=20)

textoinicial = ctk.CTkLabel(frame_inicial, text='Bem vindo ao SADAC', font=('Times New Roman', 24))
textoinicial.pack(pady=30)

significado = ctk.CTkLabel(frame_inicial, text='Sistema de AudioDescrição das Ârvores Ceturianas')
significado.pack(pady=0)

mapa = ctk.CTkButton(frame_inicial, text='Abrir Mapa', font=('Times New Roman', 20), command=mapasadc,height=40)
mapa.pack(pady=20)

sair = ctk.CTkButton(frame_inicial, text='Sair',font=('Times New Roman', 20), command=fechar,height=40)
sair.pack(pady=20)

arboreio.mainloop()
