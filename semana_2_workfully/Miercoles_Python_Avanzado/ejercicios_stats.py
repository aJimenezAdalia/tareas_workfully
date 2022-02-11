

# EJERCICIO 1
# Importa las librerías
import numpy as np
import pandas as pd

# EJERCICIO 2
# 1. Importa el dataset "datasets_beer.csv"
beers = pd.read_csv('/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/5 - Stats/datasets_beers.csv')
# 2. Imprime por pantalla los primeros registros.
beers.head()
# 3. ¿Cuáles son sus columnas?
beers.columns
# 4. ¿Qué dimensiones tiene el DataFrame?
beers.shape

# EJERCICIO 3
# Elimina la columna Unnamed: 0
beers.drop('Unnamed: 0', axis=1, inplace=True)

# EJERCICIO 4
beers.shape

# EJERCICIO 5
# De qué tipo son los datos?
beers.dtypes

# EJERCICIO 6
# Obtén en una nuevo DataFrame un resumen con las principales estadísticas de las
# columnas numércias: mean, max, count, cuantiles...
beers.describe()

# EJERCICIO 7
# ¿Cuántas birras hay de cada estilo en este dataset?
# Investiga en la documentación de Series si puedes hacer un conteo de valores.
beers.value_counts()

# EJERCICIO 8
# 1. Imprime por pantalla los registros del 10 al 20
beers[10:21]
# 2. De esos registros, imprime por pantalla desde la columna name a ounces , ambas incluidas
beers.loc[10:20, 'name': 'ounces']
# 3. Quédate con las columnas abv , ibu y ounces ,
# y además quédate sólo con los registros 10 al 20.
apartado_3 = beers.loc[10:20, ['abv', 'ibu', 'ounces']]
# 4. Convierte el resultado del apartado 3 en un array de numpy
np.array(apartado_3)

# EJERCICIO 9
# ¿Cuántas onzas pesan todas las birras del dataset?
beers.ounces.sum()

# EJERCICIO 10
# El amargor de las cervezas se mide por su nivel de IBUs.
# 1. ¿Cuál es el amargor medio de las cervezas?
beers.ibu.mean()
# 2. ¿El máximo? ¿Y el mínimo?
beers.ibu.max()
beers.ibu.min()
# 3. ¿Qué cerveza es la que tiene el amargor máximo? ¿Cuál es la de amargor mínimo?
maximo_amargor = beers[beers.ibu == beers.ibu.max()]['name'].values[0]
minimo_amargor = beers[beers.ibu == beers.ibu.min()]['name'].values[0]

# EJERCICIO 11
# No queda muy claro cuánto de dispar, de dispersa, es la medida de IBU. Mediante estadística
# descriptiva (una o dos métricas, sin gráficas), razona la dispersión de la variable IBU.
beers.ibu.min()
beers.ibu.max()
beers.ibu.std()

# EJERCICIO 12
# ¿Existe alguna relación lineal entre las variables numéricas del dataset?
# Intenta pintar este razonmiento mediante un gráfico
variables_numericas = [col for col in beers.columns if beers[col].dtype in ['float64', 'int64']]

import seaborn as sns
sns.heatmap(beers[variables_numericas].corr(), cmap='Greens', annot=True);

# EJERCICIO 13
# Representa el nivel de alcohol (columna abv ) en un histograma.
# ¿Se trata de una distribución simétrica o asimétrica?
sns.histplot(beers.abv);

# EJERCICIO 14
# Representa mediante un boxplot de seaborn la variable abv
sns.boxplot(beers.abv);

# EJERCICIO 15
# 1. ¿Qué estilos son los que tienen en media más alcohol?
beers.groupby('style').agg({'abv': 'mean'}).sort_values('abv', ascending=False).head()
# 2. ¿Y los estilos que son en media más amargos?
beers.groupby('style').agg({'ibu': 'mean'}).sort_values('ibu', ascending=False).head()

# EJERCICIO 16
# Carga el datasets de cervecerias datasets_breweries.csv
breweries = pd.read_csv('/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/5 - Stats/datasets_breweries.csv')

# EJERCICIO 17
# Renombra la columna Unnamed: 0 como brewery_id
# Renombra la columna name por brewery_name
# Hazlo en una sola sentencia
rename_cols = {'Unnamed: 0': 'brewery_id', 'name': 'brewery_name'}
breweries = breweries.rename(columns=rename_cols)

# EJERCICIO 18
# Junta los dos datasets que tienes
full_data = pd.concat([beers, breweries], axis=1)

# EJERCICIO 19
# 1. ¿Cuántos estados diferentes hay?
full_data.state.nunique()
# 2. ¿Y ciudades diferentes?
full_data.city.nunique()
# 3. ¿Cuántas vervecerías hay?
full_data.brewery_id.nunique()

# EJERCICIO 20
# Agrupa por estado y ciudad, la media, la mediana y el max nivel de alcohol
full_data.groupby(['state', 'city']).agg({'abv': 'mean'})
full_data.groupby(['state', 'city']).agg({'abv': 'median'})
full_data.groupby(['state', 'city']).agg({'abv': 'max'})

# EJERCICIO 21
# ¿Cuáles son las cervezas más amargas que se consumen en Indiana, estado = IN ?
indiana = full_data[full_data.state == ' IN']

# EJERCICIO 22
# Obtén una tabla con los principales estadísticos del campo ibu , a nivel ciudad
full_data[['city', 'ibu']].describe()

# EJERCICIO 23
# Consigue en un DataFrame todas las cervezas en cuyas cervecerías
# el mínimo nivel de abv sea de 0.07.
full_data[full_data.abv <= 0.07]['name']

# EJERCICIO 24
# Teniendo en cuenta la media de amargor de todas las cervezas, obtén una tabla
# con las cervezas cuyos estados tengan una media de amargor en cerveza por encima de la media
media_amargor = full_data.ibu.mean()
amargor = full_data.groupby('state').mean()[['name', 'ibu']]
amargor[amargor.ibu > media_amargor]
