#funcion que se encarga de importar los datos y limpiarlos
import pandas as pd
import numpy as np

def limpia_datos(raw_data):
    raw_data.dropna(inplace=True)
    print(raw_data.info())
