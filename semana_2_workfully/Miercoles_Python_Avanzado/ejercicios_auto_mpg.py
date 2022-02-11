

import pandas as pd
import numpy as np

cars1_path = '/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/4 - Merge/Auto_MPG/cars1.csv'
cars2_path = '/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/3 - Python Avanzado/2 - Pandas/Practica/4 - Merge/Auto_MPG/cars2.csv'

# Variables
cars1 = pd.read_csv(cars1_path)
cars2 = pd.read_csv(cars2_path)

# Oops, it seems our first dataset has some unnamed blank columns, fix cars1
blank_cols = [col for col in cars1.columns if col.startswith('Unnamed')]
cars1 = cars1.drop(blank_cols, axis=1)

# What is the number of observations in each dataset?
cars1.size
cars2.size

# Join cars1 and cars2 into a single DataFrame called cars
cars = pd.concat([cars1, cars2], axis=0)

# Oops, there is a column missing, called owners.
# Create a random number Series from 15,000 to 73,000.
random_owners = np.random.randint(15000, 73000, 398)

# Add the column owners to cars
cars['owners'] = random_owners

#