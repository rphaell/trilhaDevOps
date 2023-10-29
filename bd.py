import sqlite3

# conectar ao banco de dados ( ou criar se não existir)

conn = sqlite3.connect('devops.bd')

# criar um cursos para executar comandos SQL
cursor = conn.cursor()

# criar uma tabela chamada "dados" com colunas "id" e "nome"

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY,
        nome TEXT
    )
''')

# salvar as alterações e fechar a conexão com o banco de dados
conn.commit()
conn.close()