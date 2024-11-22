import pandas as pd
import csv 
import sys
import os

import read_data as read

df = read.read_data()

#limpieza
def clean():
    df = read.read_raw_data()
    df = df.drop_duplicates()
    df['Attrition'].replace({'Yes': True, 'No': False}, inplace=True)
    df["YearsWithCurrManager"].fillna(0, inplace=True)
    df.columns = df.columns.str.replace("[{}()%:]",'',regex=True)
    df.drop(columns=["Over18"], inplace=True)
    df.to_csv("./source/datos/clean_analytics.csv", index=False)
    print("Datos limpios")