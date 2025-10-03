import pandas as pd

df = pd.read_csv('Statements_Midata.csv', encoding="cp1252", sep=";")
print(df.to_string())