import pandas as pd
df = pd.read_html('https://finance.naver.com/item/sise_day.nhn?code=066570')
print(df)
