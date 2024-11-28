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
    elif tipo == 4:
        graf_violi(dato)
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
    if btn_dato == "Relación Edad/Departamento":
        grouped_df = df.groupby(['Department', 'AgeGroup']).size().unstack().fillna(0)
        ax = grouped_df.plot(kind='bar', figsize=(12, 8), stacked=False)



        plt.title(f'Gráfico de Barras: {btn_dato}')
        plt.xlabel('Categoría')
        plt.ylabel('Valor')
        plt.xticks(rotation=0)
        for p in ax.patches:
            ax.annotate(str(int(p.get_height())), (p.get_x() * 1.005, p.get_height() * 1.005))
        plt.show()
        print(btn_dato)
    elif btn_dato == "Brecha salarial p/ Género (promedio)":
        import pandas as pd
        sns.barplot(x='Gender', y='MonthlyIncome', data=df, estimator=pd.Series.mean, ci=None, palette=['blue', 'pink'])

        plt.title(f'Gráfico de Barras: {btn_dato}')
        plt.xlabel('Género')
        plt.ylabel('Salario')
        plt.show()
        print(btn_dato)

def graf_cal(btn_dato):
    import numpy as np
    # Grafico de calor de valores correlacionados
    df = data.read_data()
    dfaux = df.copy()
    plt.figure(figsize=(8, 6))
    x = dfaux.select_dtypes(include= [int, float]).corr()
    #print(x)
    el = set([j if j < 0.3 else None for i in x.values for j in i])
    for i in el:
        x.replace(np.float64(i), 0, inplace= True)
    fl = set([i if x[i].values.sum() <= 1 else None for i in x.columns])
    #print(fl)
    for i in fl:
        if i != None:
            dfaux.drop([i], axis= 1, inplace= True)
            
    y = dfaux.select_dtypes(include= [int, float]).corr()
    plt.subplots_adjust(
        top=0.938,
        bottom=0.321,
        left=0.248,
        right=0.981,
        hspace=0.2,
        wspace=0.2)
    #print(y)
    sns.heatmap(y, annot=True, cmap="coolwarm")
    plt.xticks(rotation=70)
    
    plt.title(f'Gráfico de Calor: Columnas')
    plt.show()
    #print(df.select_dtypes(include=[float, int]).corr())

def graf_violi(btn_dato):
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='Gender', y='MonthlyIncome', data=df, palette=['blue', 'pink'])

    # Añadir etiquetas y título
    plt.xlabel('Género')
    plt.ylabel('Salario')
    plt.title(f'Violin Plot: {btn_dato}')

    # Mostrar el gráfico
    plt.show()

