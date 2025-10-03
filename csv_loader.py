import pandas as pd

df = pd.read_csv('Statement.csv', encoding="cp1252")
#df = pd.read_excel('Statement.xlsx')
print(df.isnull())
print(df)