

import pandas as pd

# Create the 3 DataFrames based on the following raw data
raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

# Assign each to a variable called data1, data2, data3
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

# Join the two dataframes along rows and assign all_data
all_data = pd.concat([data1, data2, data3], axis=0)

# Join the two dataframes along columns and assing to all_data_col
all_data_col = pd.concat([data1, data2, data3], axis=1)

# Print data3
print(data3)

# Merge all_data and data3 along the subject_id value
all_data.merge(data3, on='subject_id')

#  Merge only the data that has the same 'subject_id' on both data1 and data2
data1.merge(data2, on='subject_id', how='inner')

# Merge all values in data1 and data2, with matching records from both sides where available.
data1.merge(data2, how='outer')



