import pandas as pd
import csv

def read_data():
    df = pd.read_csv("source/datos/clean_analytics.csv")
    return df
def read_raw_data():
    df = pd.read_csv("source/datos/analytics.csv")
    return df
