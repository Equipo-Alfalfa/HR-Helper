#archivo principal del proyecto
import os
import pandas as pd
import numpy as np
import matplotlib as plt
import limpia_datos


data = pd.read_csv("datos/data.csv")

limpia_datos.limpia_datos(data)