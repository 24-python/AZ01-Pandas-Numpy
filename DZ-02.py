import pandas as pd

df = pd.read_csv('AAPL.csv')

print(df.head())

print(df.info())

print(df.describe())
