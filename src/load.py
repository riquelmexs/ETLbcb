
import os
import sqlite3

def salvar_csv(df, caminho="datasets/expectativa_inflacao_24_meses.csv"):
    """
    Salva o DataFrame como arquivo CSV.
    """
    os.makedirs("datasets", exist_ok=True)
    df.to_csv(caminho, index=False)

def salvar_sqlite(df, banco="datasets/dados.db", tabela="expectativa_inflacao_24_meses"):
    """
    Salva o DataFrame em um banco de dados SQLite.
    """
    os.makedirs("datasets", exist_ok=True)
    conn = sqlite3.connect(banco)
    df.to_sql(tabela, conn, if_exists="replace", index=False)
    conn.close()
