import pandas as pd
from faker import Faker
import random

# faker para generar datos falsos (creo)
fake = Faker()

# Funcion de calculo de nómina
def calculate_payroll(salary_monthly, days_worked):
    salary_daily = salary_monthly / 30
    salary_hourly = salary_daily / 8  
    total_salary = salary_daily * days_worked + extra    
    
    HENv = 0.08  # Hrs extra nocturnas valor
    HBNv = 0.16  # Hrs bono nocturno valor
    HEDv = 0.27  # Hrs extra diurnas valor
    
    HEN = HENaux * HENv  
    HBN = HBNaux * HBNv # Cálculos de pago por hrs extra
    HED = HEDaux * HEDv  
    extra = HEN + HBN + HED

    IVSS = 2.24
    RPE = 0.43  # Retenciones varias
    FAOV = 0.86
    
    tax = IVSS + RPE + FAOV
    total_to_pay = total_salary - tax
    return salary_daily, salary_hourly, HENv, HBNv, HEDv, total_salary, tax, total_to_pay

# lista para guardar datos
data = []

# 100 entradas falsas para nuestra prueba
def excel_gen():
    for _ in range(100):
        salary_monthly = fake.random_int(min=130, max=500)  # Random sal mensual
        days_worked = fake.random_int(min=20, max=30)  # Random dias trabajados
    
        HBNaux = fake.random_int(min=0, max=2)
        HEDaux = fake.random_int(min=0, max=2)
        HENaux = fake.random_int(min=0, max=2)
    
        # calcular valores de la nómina
        salary_daily, salary_hourly, total_salary, deductions, total_to_pay = calculate_payroll(salary_monthly, days_worked)

        entry = {
            "Cédula de Identidad": fake.random_int(min=10000000, max=99999999),
            "Nombre del Trabajador": fake.name(),
            "Cargo": fake.job(),
            "Fecha de Ingreso": fake.date_between(start_date='-3y', end_date='today'),
            "Salario Mensual": salary_monthly,
            "Salario Básico Diario": salary_daily,
            "Salario por Hora": salary_hourly,
            "Días Trabajados": days_worked,
            "HEN": HENv,
            "HBN": HBNv,
            "HED": HEDv,
            "Cantidad HEN": HENaux,
            "Cantidad HBN": HBNaux,
            "Cantidad HED": HEDaux,
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
