import tkinter
from tkinter import simpledialog, messagebox
from core.conexao import conexaoBanco


# Função para validar a senha antes de acessar a página de registro
def solicitarSenha(registro):
    senha_admin = simpledialog.askstring(
        "Senha Requerida", "Digite a senha de administrador para continuar:", show="*"
    )
    if senha_admin == "123":  # Substitua "123" pela sua senha desejada
        messagebox.showinfo("Acesso Permitido", "Senha correta! Acessando registro.")
        registro()  # Chama a página de registro
    else:
        messagebox.showerror("Acesso Negado", "Senha incorreta. Tente novamente.")

def loginUsuario(janela, termo1, termo2):
    usuario = termo1.get()
    senha = termo2.get()

    # Conectar ao banco de dados
    conexao = conexaoBanco()
    cursor = conexao.cursor()

    try:
        # Consulta SQL para validar login e obter tipo de usuário
        cursor.execute(
            "SELECT tipo_usuario FROM perfis WHERE login = %s AND senha = %s",
            (usuario, senha)
        )
        resultado = cursor.fetchone()  # Retorna a primeira linha encontrada

        if resultado:
            tipo_usuario = resultado[0]  # Pega o valor de 'tipo_usuario'
            messagebox.showinfo("Login Bem-Sucedido", f"Bem-vindo, {usuario}!")

            # Fecha a janela de login
            janela.destroy()

            # Redireciona com base no tipo de usuário
            if tipo_usuario == "administrador":
                menu_adm.iniciar(usuario)
            elif tipo_usuario == "aluno":
                menu_home.iniciar(usuario)
            elif tipo_usuario == "professor":
                from interface.login.pagina_prof import menu_prof
                menu_prof.iniciar(usuario)
            else:
                messagebox.showerror("Erro", "Tipo de usuário desconhecido.")
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos. Tente novamente.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco: {e}")
    finally:
        # Fechar conexão com o banco
        cursor.close()
        conexao.close()

        
# Função para salvar os dados no banco de dados
def salvarDados(pagina ,nome, email, login, senha, tipo_usuario):
    # Obtém os valores dos campos
    nome_valor = nome.get()
    email_valor = email.get()
    login_valor = login.get()
    senha_valor = senha.get()
    tipoUsuario_valor = tipo_usuario.get()  # Obtém o valor selecionado no OptionMenu

    # Valida se todos os campos estão preenchidos
    if not nome_valor or not email_valor or not login_valor or not senha_valor:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    try:
        # Conecta ao banco usando o util.db
        conexao = conexaoBanco()
        if conexao:
            cursor = conexao.cursor()

            # Insere os dados na tabela "usuarios"
            cursor.execute("""
                INSERT INTO perfis (nome, email, login, senha, tipo_usuario) 
                VALUES (%s, %s, %s, %s, %s)
            """, (nome_valor, email_valor, login_valor, senha_valor, tipoUsuario_valor))

            # Confirma as alterações no banco
            conexao.commit()
            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")

            # Fecha a conexão e o cursor
            cursor.close()
            conexao.close()

            # Fecha a janela de registro
            pagina.destroy()
        else:
            messagebox.showerror("Erro", "Não foi possível conectar ao banco de dados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar: {e}")