

# Ejercicio 1
import pandas as pd

print(pd.__version__)

# Ejercicio 2
df = pd.read_csv('/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/0 - Basics/laliga.csv')

# Ejercicio 3
df.head(4)

# Ejercicio 4
import numpy as np

valores_df = np.array(df)

# Ejercicio 5
print(df.columns)

# Ejercicio 6

# Manera 1
poblacion1 = pd.Series(
    {'Madrid': 6685471,
     'Galicia': 2698764,
     'Murcia': 1494442,
     'Andalucía': 8446561})

# Manera 2
comunidades = list(poblacion1.index)
poblaciones = poblacion1.values

poblacion2 = pd.Series(data=poblaciones, index=comunidades)

# Ejercicio 7
array_valores = np.array(poblacion2.values)
array_indices = np.array(poblacion2.index)
valores_indices = [valor for valor in array_indices]

# Ejercicio 8
poblacion_primer_elemento = poblacion2[0]
poblacion_galicia = poblacion2['Galicia']
poblaciones_pedidas = poblacion2['Galicia': 'Andalucía']
print('Galicia' in poblacion2.index)

poblacion_primer_elemento_ = poblacion2.iloc[0]
poblacion_galicia_ = poblacion2[poblacion2.index == 'Galicia'].values[0]
poblaciones_pedidas_ = poblacion2.iloc[1:]

# Ejercicio 9
tasas_paro = {
    'Madrid': 9.99,
    'Galicia': 11.74,
    'Murcia': 16.08,
    'Andalucía': 20.8}
data = pd.DataFrame(
    data=[poblacion2, pd.Series(tasas_paro)]).T
data.columns = ['poblacion', 'tasa_paro']
data

# Ejercicio 10
print(data.poblacion)
print(data.tasa_paro)

# Ejercicio 11
superficie_ccaa = {
    'Madrid': 8028,
    'Galicia': 29575,
    'Murcia': 11314,
    'Andalucía': 87599
}

data2 = pd.concat([data, pd.Series(superficie_ccaa, name='superficie')], axis=1)
data2

# Ejercicio 12
data2['densidad_poblacion'] = data2.poblacion / data2.superficie

