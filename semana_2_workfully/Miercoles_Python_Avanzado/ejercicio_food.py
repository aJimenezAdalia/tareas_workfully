

import pandas as pd
import numpy as np

# Loading the data
food = pd.read_csv('/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/1 - Getting and Knowing your data/World Food Facts/food_100.csv')

# First 5 entries
food.head()

# Number of observations
food.size

# Number of columns
len(food.columns)

# Name of the columns
print(food.columns)

# Name of 105th column
print(food.columns[104])

# Type of observations of the 105th column
food[food.columns[104]].dtype

# Indexes
food.index

# 19th product name
food.loc[19, 'product_name']


