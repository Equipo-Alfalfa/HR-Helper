def buscar_usuarios_por_id(id):
    import pandas as pd
    import read_data as read
    df = read.read_data()
    empleado = df.loc[df["EmpID"] == id] 
    return empleado