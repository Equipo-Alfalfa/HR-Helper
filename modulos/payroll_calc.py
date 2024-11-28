import pandas as pd
import openpyxl
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulos')))
import modulos.read_data as data
df = data.read_data()

needed_col = df[["Name","C.I","DaysWorked","MonthlyIncome","JobRole","HBN","HEN","HED"]]

needed_col.to_excel("./source/datos/payroll.xlsx", index=False, engine="openpyxl")

# Funcion de calculo de nómina
def calculate_payroll(file_path):
    pay_df = pd.read_excel(file_path)
    res = []

    for index,row  in pay_df.iterrows():

        salary_monthly =row["MonthlyIncome"]
        days_worked = row["DaysWorked"]

        salary_daily = salary_monthly / 30  # empieza el calculo de salario 
        salary_hourly = salary_daily / 8      
    
        HENaux = row["HEN"]
        HBNaux = row["HBN"] # extraccion de datos de las columnas
        HEDaux = row["HED"]

        HENv = 0.08  
        HBNv = 0.16  # Valor de cada uno de los tipos de hora extra
        HEDv = 0.27  
    
        HEN = HENaux * HENv  
        HBN = HBNaux * HBNv # Cálculos de pago por hrs extra
        HED = HEDaux * HEDv  
        extra = HEN + HBN + HED

        IVSS = 2.24
        RPE = 0.43  # Retenciones varias
        FAOV = 0.86
        tax =  IVSS + RPE + FAOV

        total_salary = salary_daily * days_worked + extra
        total_to_pay = total_salary - tax

        # Agregar datos al excel
        res.append({
            "Nombre del empleado":row["Name"],
            "Cédula": row["C.I"],
            "Cargo": row["JobRole"],
            "Salario mensual básico": row["MonthlyIncome"],
            "HEN":HEN,
            "HBN":HBN,
            "HED":HED,
            "Pago extra total": extra,
            "Retenciones totales": tax,
            "Total a pagar": total_to_pay,
        })

        # Guardar resultados en excel
        res_df = pd.DataFrame(res)
        res_df.to_excel("./salidas/pagosnomina.xlsx", index=False, engine = "openpyxl")

    return res_df

