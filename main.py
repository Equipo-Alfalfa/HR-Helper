import pandas as pd
import datacleaning as data
import csv 
#lee cvv principal
df = pd.read_csv("analytics.csv")

datos = data.clean(df)

print (datos.head(5))