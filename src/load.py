import pandas as pd

def saveCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    df.to_csv(f'src/datasets/{nome_arquivo}.csv', decimal=decimal, sep=separador)