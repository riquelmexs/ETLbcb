# main.py

from src.extractTransform import extrair_transformar
from src.load import salvar_csv, salvar_sqlite

def main():
    print("Executando ETL da Expectativa de Inflação 24 Meses...")
    df = extrair_transformar()
    salvar_csv(df)
    salvar_sqlite(df)
    print("ETL concluído com sucesso! Dados salvos em CSV e SQLite.")

if __name__ == "__main__":
    main()
