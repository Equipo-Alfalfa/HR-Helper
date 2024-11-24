import pandas as pd
from faker import Faker
import random

# ESTE CODIGO AUN NO FUNCIONA FALTA LA SUMA DE LAS HRS EXTRA

# faker para generar datos falsos (creo)
fake = Faker()

# Funcion de calculo de nómina
def calculate_payroll(salary_monthly, days_worked):
    salary_daily = salary_monthly / 30
    salary_hourly = salary_daily / 8  
    total_salary = salary_daily * days_worked     
    HENv = 0.08  # Hrs extra nocturnas valor
    HBNv = 0.16  # Hrs bono nocturno valor
    HEDv = 0.27  # Hrs extra diurnas valor

    HENc = 0  # cantidad HEN
    HBNc = 0  # cantidad HBN
    HEDc = 0  # cantidad HED
    
    IVSS = 2.24
    RPE = 0.43
    FAOV = 0.86
    tax = IVSS + RPE + FAOV
    total_to_pay = total_salary - tax
    return salary_daily, salary_hourly, HEN, HBN, HED, total_salary, tax, total_to_pay

# lista para guardar datos
data = []

# 100 entradas falsas para nuestra prueba
def excel_gen():
    for _ in range(100):
        salary_monthly = fake.random_int(min=130, max=500)  # Random sal mensual
        days_worked = fake.random_int(min=20, max=30)  # Random dias trabajados
    
        HBN = fake.random_int(min=0, max=2)
        HED = fake.random_int(min=0, max=2)
        HEN = fake.random_int(min=0, max=2)
    
        # calcular valores de la nómina
        salary_daily, salary_hourly, total_salary, deductions, total_to_pay = calculate_payroll(salary_monthly, days_worked)

        entry = {
            "Cédula de Identidad": fake.random_int(min=10000000, max=99999999),
            "Nombre del Trabajador": fake.name(),
            "Cargo": fake.job(),
            "Fecha de Ingreso": fake.date_between(start_date='-3y', end_date='today'),
            "Salario Mensual": salary_monthly,
            "Salario Básico Diario": salary_daily,
            "Salario por Hora": 
            salary_hourly,
            "Días Trabajados": days_worked,
            "HEN": HEN,
            "HBN": HBN,
            "HED": HED,

            "Cantidad HEN": 
            "Cantidad HBN": 
            "Cantidad HED": 
            
            "Total Salario": total_salary,
            "IVSS": IVSS,
            "RPE": RPE,
            "FAOV": FAOV,
            "Deducción Total": tax,
            "Total a Pagar": total_to_pay,
        }
        data.append(entry)
    df = pd.DataFrame(data)
    # Exportar a un excel
    df.to_excel('nomina.xlsx', index=False)

    print("Dataset guardado en 'nomina.xlsx'.")

excel_gen()