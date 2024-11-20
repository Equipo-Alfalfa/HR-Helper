import pandas as pd
import csv 

#limpieza
def clean(df):
    df = df.drop_duplicates()
    df["YearsWithCurrManager"].fillna(0, inplace=True)
    df.columns = df.columns.str.replace("[{}()%:]",'',regex=True)
    df.drop(columns=["Over18"], inplace=True)
    df.to_csv("analitycs.csv", index=False)
    
    return df
