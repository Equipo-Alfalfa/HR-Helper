import pandas as pd
import matplotlib.pyplot as plt
import modulos.read_data as data
import seaborn as sns

df = data.read_data()

def graficar(tipo, dato):
    if tipo == 1:
        graf_pie(dato)
    elif tipo == 2:
        graf_cal(dato)
    elif tipo == 3:
        graf_bar(dato)
    else:
        print("error")

def graf_pie(btn_dato):

    if btn_dato == "Campo de Educación":
        dato = "EducationField"
    elif btn_dato == "Rangos de Edad":
        dato = "AgeGroup"
    else:
        print("Ha ocurrido un error")

    frecuencia = df[dato].value_counts()

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        frecuencia,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        pctdistance=1.18
    )

    ax.set_title(f'grafico de pastel: {btn_dato}', fontsize=16)

    ax.legend(wedges, frecuencia.index, title=btn_dato, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.subplots_adjust(left=0.1, right=0.75)

    plt.savefig('source/grafico_pastel.png')

    plt.ylabel('')
    plt.show()
    print(dato)

def graf_bar(btn_dato):
    grouped_df = df.groupby(['Department', 'AgeGroup']).size().unstack().fillna(0)
    ax = grouped_df.plot(kind='bar', figsize=(12, 8), stacked=False)



    # Añadir título y etiquetas a los ejes
    plt.title(f'Gráfico de Barras: {btn_dato}')
    plt.xlabel('Categoría')
    plt.ylabel('Valor') # Mostrar el gráfico

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.show()
    print(btn_dato)

def graf_cal(btn_dato):
    df = data.read_data()
    df_corr = df[["Attrition", "Age", "DistanceFromHome"]]
    corr_matrix = df_corr.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title(f'Gráfico de Calor: {btn_dato}')
    plt.show()
    print(btn_dato)