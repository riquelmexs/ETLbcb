import requests
import pandas as pd

def ETLbcb(data: str) -> pd.DataFrame:

    """"

    função para extrair os dados da API do banco central.

    Atributo
    AAAAT - String - A Ano e T trimestre (1-4) apartir de 

    saída:
    DataFrame com os dados econômicos dos meios de Pagamento.
    """
    url=f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='20051'&$format=json"
    req = requests.get(url)
    print("Status Code:", req.status_code)
    data = req.json()

    df = pd.json_normalize(data["Value"])
    
    df['datatrimestre'] = pd.to_datatime(df['datatrimestre'])
    return df


