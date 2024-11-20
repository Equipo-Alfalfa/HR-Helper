import pandas as pd
import csv

def read_data():
    df = pd.read_csv("analytics.csv")
    return df
