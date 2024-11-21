import pandas as pd
import csv

def read_data():
    df = pd.read_csv("source/datos/analytics.csv")
    return df
