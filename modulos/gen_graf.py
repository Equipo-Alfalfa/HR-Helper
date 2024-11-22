import pandas as pd
import matplotlib.pyplot as plt
import modulos.read_data as data
import seaborn as sns

def graf_pie(column):
    df = data.read_data()
    column = "EducationField"
    frecuencia = df[column].value_counts()

    fig, ax = plt.subplots()
    frecuencia.plot.pie(
        autopct='%1.1f%%',  
        startangle=90,      
        shadow=True,        
        figsize=(8, 8)      
    )

    ax.set_title('Campo de educación de los empleados', fontsize=16)

    plt.savefig('source/grafico_pastel.png')

    plt.ylabel('')
    plt.show()

def graf_bar(column):
    df = data.read_data()
    grouped_df = df.groupby(['Department', 'AgeGroup']).size().unstack().fillna(0)
    ax = grouped_df.plot(kind='bar', figsize=(12, 8), stacked=False)



    # Añadir título y etiquetas a los ejes
    plt.title('Gráfico de Barras: Relación entre Categoría y Valor')
    plt.xlabel('Categoría')
    plt.ylabel('Valor') # Mostrar el gráfico

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.show()
