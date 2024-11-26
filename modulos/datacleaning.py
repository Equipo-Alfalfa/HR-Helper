import read_data as read
from faker import Faker
import random
import numpy as np

fake = Faker()

# CONSTANTES

CImin = 10000000
CImax = 99999999
workedMin = 20
workedMax = 30
extraMin = 0
extraMax = 2

def clean():
    try:
        df = read.read_raw_data()
       
       # Limpieza
        df = df.drop_duplicates()
        df['Attrition'].replace({'Yes': True, 'No': False}, inplace=True)
        df["YearsWithCurrManager"].fillna(0, inplace=True)
        df.columns = df.columns.str.replace("[{}()%:]",'',regex=True)
        df.drop(columns=["Over18"], inplace=True)
        df.drop(columns=["OverTime"], inplace=True)
    
        # generación de cédulas aleatorias y únicas
        random.seed(42)
        aux = random.sample(range(10000000, 100000000), len(df))
        df["C.I"] = aux
        
        #adición de hrs extra, nombres y dias trabajados en el mes
        df["Name"] = [fake.name() for _ in range (len(df))]
        df["Days worked"] = np.random.randint(DAYS_WORKED_MIN, DAYS_WORKED_MAX + 1, size=len(df))
        df["HBN"] = np.random.randint(HBN_HED_HEN_MIN, HBN_HED_HEN_MAX + 1, size=len(df))
        df["HED"] = np.random.randint(HBN_HED_HEN_MIN, HBN_HED_HEN_MAX + 1, size=len(df))
        df["HEN"] = np.random.randint(HBN_HED_HEN_MIN, HBN_HED_HEN_MAX + 1, size=len(df))

        # Guardar
        df.to_csv("./source/datos/clean_analytics.csv", index=False)
        print("Datos limpios")

    except Exception as e:
        print(f"An error ocurred: {e}")

clean()
