import numpy as np
import pandas as pd
# Cepeda Darrell NC = 0030
## datos matriz 4 x 3
datos_alumno = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]
# poner nombre a las columnas
# y almacenar la tabla en la variable df DataFrame
print("----- datos a partir de una matriz 4 x 3 ----")
df=pd.DataFrame(datos_alumno,columns=["ci","marcas","paquete"])
print(df)
# datos a partir de un diccionario
print("---- datos a partir de un diccionario ----")
alumno_diccionario={
    "nombre":["Allison","Alexia","Iris","Jairo","Nicole","Caleb"],
    "califa":[90,60,100,60,100,70],
    "edad":[15,17,17,16,16,15]
}

estudiantes = pd.DataFrame(alumno_diccionario)
print(estudiantes)

print("Programa ejecutado por Cepeda Darrell Nc = 0030")