import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
df = pd.read_csv("analytics.csv")

# Contar la frecuencia de cada valor en la columna 'Categoría'
frecuencia = df['EducationField'].value_counts()

# Crear el gráfico de pastel
fig, ax = plt.subplots()
frecuencia.plot.pie(
    autopct='%1.1f%%',  # Mostrar porcentajes con un decimal
    startangle=90,      # Iniciar desde el ángulo 90
    shadow=True,        # Añadir sombra
    figsize=(8, 8)      # Tamaño de la figura
)

# Añadir título
ax.set_title('Campo de educación de los empleados', fontsize=16)

# Guardar el gráfico como PNG
plt.savefig('source/grafico_pastel.png')

# Mostrar el gráfico
plt.ylabel('')
plt.show()

