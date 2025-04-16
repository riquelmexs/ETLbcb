import sqlite3

# Cria conexão com o banco
conn = sqlite3.connect("dados_bcb.db")
cursor = conn.cursor()

# Exemplo de criação de tabela (adapte conforme seus dados)
cursor.execute("""
CREATE TABLE IF NOT EXISTS indicadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    valor REAL,
    data TEXT
)
""")

conn.commit()
conn.close()
