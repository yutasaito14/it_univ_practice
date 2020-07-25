import pandas as pd


df=pd.read_csv("test.csv")


print(df)

kokugo = df.values
kokugo.to_csv("export1.csv")


