import pandas as pd
import matplotlib.pyplot as plt
import modulos.read_data as data
import seaborn as sns


def graficar(tipo, dato):
    if tipo == 1:
        graf_pie(dato)
    elif tipo == 2:
        pass
    elif tipo == 3:
        graf_bar(dato)
    else:
        print("error")


def graf_pie(dato):
    df = data.read_data()
    column = "EducationField"
    frecuencia = df[column].value_counts()

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        frecuencia,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        pctdistance=1.18
    )

    ax.set_title(f'grafico de pastel: {dato}', fontsize=16)

    # Añadir la leyenda al lado
    ax.legend(wedges, frecuencia.index, title="Campo de Educación", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Ajustar el diseño para que la leyenda no solape el gráfico
    plt.subplots_adjust(left=0.1, right=0.75)

    plt.savefig('source/grafico_pastel.png')

    plt.ylabel('')
    plt.show()
    print(dato)

def graf_bar(dato):
    df = data.read_data()
    grouped_df = df.groupby(['Department', 'AgeGroup']).size().unstack().fillna(0)
    ax = grouped_df.plot(kind='bar', figsize=(12, 8), stacked=False)



    # Añadir título y etiquetas a los ejes
    plt.title(f'Gráfico de Barras: {dato}')
    plt.xlabel('Categoría')
    plt.ylabel('Valor') # Mostrar el gráfico

    for p in ax.patches:
        ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005))
    plt.show()
    print(dato)
