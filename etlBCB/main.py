import requests
import pandas as pd


def etlBcB(data):
    """
    Função para extrair os dados da API do Banco Central.
    """
    url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    data = req.json()

    df = pd.json_normalize(data["value"])
    # print(df)
    return df
