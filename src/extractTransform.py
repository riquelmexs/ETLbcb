
import requests
import pandas as pd

def extrair_transformar():
    """
    Extrai dados da API do Banco Central (Expectativa de Inflação em 24 meses)
    e retorna um DataFrame com a coluna DataReferencia criada manualmente.
    """
    url = "https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoInflacao24Meses?$top=1000&$format=json"
    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data["value"])

    # Adiciona uma coluna de data incremental se não existir
    if "DataReferencia" not in df.columns:
        df["DataReferencia"] = pd.date_range(start="2022-01-01", periods=len(df), freq="W")

    return df
