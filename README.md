
# HR HELPER

Este proyecto espera ayudar a trabajadores relacionados al area de recursos humanos a obtener pistas visuales a partir de los datos contenidos en archivos .csv para poder tomar decisiones relacionadas a los factores que afectan el performance de sus empleados, satisfaccion laboral, ademas de obtener insights valiosos respecto al pago de dichos empleados.

El dataset fué extraido de https://www.kaggle.com/datasets/rishikeshkonapure/hr-analytics-prediction.

Durante la limpieza de datos en "dataCleaning.py" se generaron columnas artificiales de datos nuevos usando los módulos numpy, faker y random para obtener los datos necesarios para rellenar el formato de un archivo de nómina como lo vendrían siendo la cantidad de días trabajados en el mes o la cantidad y tipo de horas extras realizadas por día del mes.

En el directorio "source" se encuentran los assets utilizados para el GUI en las carpetas llamadas "icons" e "imagenes", en cambio en la carpeta denominada "datos" está el dataset original, el dataset limpio y el archivo de nómina antes de ser operado.

En "salidas" se encuentran archivos operados como el excel que contiene los pagos de la nómina.

Todas las funciones se encuentran en el directorio de "módulos", entre ellas sew destacan un buscador de empleados que tiene como salida ciertos datos relevantes del mismo, una función de filtrado de datos para encontrar grupos de empleados que coinciden con cierta caractaristica (como los salarios), un generador de gráficos que destaca información relevante para la gestión de talento humano y una calculadora de pagos de nómina la cual extrae columnas de un csv para convertirlas en un excel para calcular el pago neto.

El programa se construye a partir del archivo "setup.py" generando un ejecutable.
para esto puedes instalar las dependencias con pip freeze: pip install -r requirements.txt

si deseas ejecutar el programa en un SO distinto a windows puedes ejecutar el archivo mainUI.py luego de haber instalado las dependencias necesarias con el paso anterior

para ejecutar el programa puedes descargar el zip en releases y ejecutar el archivo .exe

# TO DO:
- Optimizar código para ejecuciones más rápidas
- Añadir nuevas gráficas
- Reorganizar y renombrar archivos, variables y funciones para cumplir con las convenciones

# PREVIEW:

https://github.com/user-attachments/assets/d13782b7-7f23-444a-a5ae-157d1582c511
