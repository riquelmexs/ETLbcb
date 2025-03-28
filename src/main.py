from src.extractTransform import ETLbcb
from src.load import saveCsv

df = ETLbcb('20191')

saveCsv(df, "meiosPagamentostri", ";", ".")