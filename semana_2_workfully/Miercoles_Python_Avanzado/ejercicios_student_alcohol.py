

import pandas as pd

address = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'

# assign the dataset to a variable called df
df = pd.read_csv(address)

# For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
df = df.loc[:, 'school': 'guardian']

# Create a lambda function that will capitalize strings.
capitalize_function = lambda x: x.capitalize()

# Capitalize both Mjob and Fjob
df.Mjob = df.Mjob.apply(capitalize_function)
df.Fjob = df.Fjob.apply(capitalize_function)

# Print the last elements of the dataset
print(df.tail())

# Did you notice the original dataframe is still lowercase? Why is that?
# Fix it and capitalize Mjob and Fjob.
'''Already done'''

# Create a function called majority that returns a boolean value to a new column called
# legal_drinker (Consider majority as older than 17 years old)
majority = lambda x: x > 17
df['legal_drinker'] = df.age.apply(majority)

# Multiply every number of the dataset by 10.
numeric_cols = [col for col in df.columns if df[col].dtypes in ['float64', 'int64']]
df[numeric_cols] = df[numeric_cols] * 10