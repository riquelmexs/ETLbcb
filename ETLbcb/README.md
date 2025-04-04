# Projeto ETL - Banco Central do Brasil

## 📌 Sobre o Projeto
Este projeto faz a extração, transformação e carga (ETL) de dados do Banco Central do Brasil.  

### 📝 Função `salvarCSV`
A função `salvarCSV` recebe um DataFrame e salva os dados em um arquivo CSV.  

```python
def salvarCSV(df, nome_arquivo):
    """
    Salva um DataFrame em um arquivo CSV.

    Parâmetros:
    df (DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): Nome do arquivo de saída.

    Retorno:
    None
    """
    df.to_csv(nome_arquivo, index=False, encoding="utf-8")
