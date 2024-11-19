import pandas as pd
import csv 

df = pd.read_csv("analytics.csv")

df = df.drop_duplicates()
df.to_csv("clean_analytics.csv", index=False)

cleanDf=read_csv("clean_analytics.csv")
print(cleanDf)