import pandas as pd

def salvarCSV(df, nome_arquivo):
    """
    Salva um DataFrame em um arquivo CSV.

    Parâmetros:
    df (DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): Nome do arquivo de saída.

    Retorno:
    None
    """
    try:
        df.to_csv(nome_arquivo, index=False, encoding="utf-8")
        print(f"✅ Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {e}")
