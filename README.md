# Análise Expectativa de Inflação - Data Science 2025.1

Projeto ETL com dados da API do Banco Central do Brasil.

## Dados Utilizados
- Fonte: [ExpectativasMercadoInflacao24Meses](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/aplicacao)
- Variável: Expectativa de inflação acumulada em 24 meses

## Estrutura
- `main.py`: pipeline ETL
- `src/extractTransform.py`: extração de dados via API
- `src/load.py`: salvamento em CSV e SQLite
- `Relatorio.ipynb`: análise estatística
- `datasets/`: saída dos dados

## Resultados
- Média estimada de inflação: ~4,30%
- Desvio padrão: ~0,25%
- Tendência de leve queda nas projeções de inflação
