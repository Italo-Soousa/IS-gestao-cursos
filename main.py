import tkinter as tk
from tkinter import PhotoImage
from core.usuario import loginUsuario, solicitarSenha, salvarDados
import os

def LoginUsuario():

    # Configuração da janela principal
    janela = tk.Tk()
    janela.title('Login Usuário')
    janela.geometry('280x300')
    janela.resizable(False, False)

    # Imagem CEUB
    diretorio_atual = os.path.dirname(__file__)
    caminho_imagem = os.path.join(diretorio_atual, "assets", "uniceub.png")
    logo_img = PhotoImage(file=caminho_imagem)

    logo_label = tk.Label(janela, image=logo_img, bd=0, relief="solid")
    logo_label.place(x=95, y=0)

    # Label "Login"
    label_login = tk.Label(janela, text="LOGIN")
    label_login.place(x=105, y=70)  # Posiciona a label "LOGIN"
    term1 = tk.Entry(janela, width=25)
    term1.place(x=25, y=105)  # Posiciona o campo de entrada do login

    # Label "Senha"
    label_senha = tk.Label(janela, text="SENHA")
    label_senha.place(x=105, y=145)  # Posiciona a label "SENHA"
    term2 = tk.Entry(janela, width=25)
    term2.place(x=25, y=180)  # Posiciona o campo de entrada da senha

    # Botões
    btn_login = tk.Button(janela, text="Entrar", command= lambda: loginUsuario(janela, term1, term2))
    btn_login.place(x=15, y=240)  # Posiciona o botão de login

    # Executar o loop principal da janela
    janela.mainloop()

def abrirPaginaRegistro():
    # Cria uma nova janela para a página de registro
    pagina_registro = tk.Toplevel()
    pagina_registro.title("Página de Registro")
    pagina_registro.geometry("300x430")
    pagina_registro.resizable(False, False)

    # Label "Nome"
    nome = tk.Label(pagina_registro, text="NOME")
    nome.pack(pady=(10, 5))
    PegandoNome = tk.Entry(pagina_registro, width=25)
    PegandoNome.pack(pady=(0, 5))

    # Label "E-mail"
    email = tk.Label(pagina_registro, text="EMAIL")
    email.pack(pady=(10, 5))
    PegandoEmail = tk.Entry(pagina_registro, width=25)
    PegandoEmail.pack(pady=(0, 5))

    # Label "Login"
    login = tk.Label(pagina_registro, text="LOGIN")
    login.pack(pady=(10, 5))
    PegandoLogin = tk.Entry(pagina_registro, width=25)
    PegandoLogin.pack(pady=(0, 15))

    # Label "Senha"
    senha = tk.Label(pagina_registro, text="SENHA")
    senha.pack(pady=(10, 5))
    PegandoSenha = tk.Entry(pagina_registro, width=25, show="*")
    PegandoSenha.pack(pady=(0, 20))

    # Label "Tipo de Usuário"
    tipo_usuario_label = tk.Label(pagina_registro, text="TIPO USUÁRIO")
    tipo_usuario_label.pack(pady=(10, 5))

    # Opções para o tipo de usuário
    tipo_usuario_opcoes = ["administrador", "professor", "aluno"]
    tipo_usuario = tk.StringVar()
    tipo_usuario.set(tipo_usuario_opcoes[0])

    tipo_usuario_menu = tk.OptionMenu(pagina_registro, tipo_usuario, *tipo_usuario_opcoes)
    tipo_usuario_menu.config(width=40,font=("Arial", 12),fg="black",bg="#ffffff",highlightthickness=1,relief="solid",bd=1)
    tipo_usuario_menu.pack(pady=(0, 20))

    # Botão para registrar
    btn_registro = tk.Button(text="Registrar", command= lambda: salvarDados(pagina_registro,PegandoNome, PegandoEmail, PegandoLogin, PegandoSenha, tipo_usuario))
    btn_registro.place(x=100, y=375)

# Chamar a função LoginUsuario para iniciar o programa
if __name__ == "__main__":
    LoginUsuario()
