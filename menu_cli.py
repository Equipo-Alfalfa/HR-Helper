import datacleaning as data
import read_data as read
def show():
    print("1. mostrar gráficos")
    print("2. mostrar datos")
    print("3. mostrar estadísticas")
    print("4. exportar datos")
    print("5. Buscar empleado")
    print("6. limpiar los datos")
    print("7. Salir")
    
    opcion = int(input("Seleccione una opció: "))
    if opcion == 1:
        men_1()
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        df = read.read_data()
        datos = data.clean(df)
        print(f"Datos limpios\n {datos.head()}")
    elif opcion == 7:
        pass

def men_1():
    print("bienvenido a la herramienta de gráficos\n seleccione un gráfico")
    print("1. cantidad de empleados por departamento")
    print("2. ")
    print("3. gráfico de lineas")