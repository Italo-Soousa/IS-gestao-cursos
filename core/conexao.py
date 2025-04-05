import mysql.connector

def conexaoBanco():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Brazil12',
            database='bd_gestaoCursos'
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Testando a conexão
con = conexaoBanco()
if con is not None and con.is_connected():
    print("✅ Conectado com sucesso ao banco de dados!")
    con.close()
else:
    print("❌ Não foi possível conectar ao banco de dados.")