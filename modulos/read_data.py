import pandas as pd

def read_data():
    import os
    archivo_path = "source/datos/clean_analytics.csv"
    if os.path.getsize(archivo_path) != 0:
        df = pd.read_csv(archivo_path)
        return df
    else:
        import GUI.limp_dial as limp_dial
        limp = limp_dial.LimpDialUI()
        limp.show_warning_dialog()

def read_raw_data():
    df = pd.read_csv("source/datos/analytics.csv")
    return df
