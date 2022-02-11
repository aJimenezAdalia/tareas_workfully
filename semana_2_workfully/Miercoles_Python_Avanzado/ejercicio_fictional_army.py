

import pandas as pd

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons'
                        , 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska',
                      'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

# Create a DF and assign it to a variable called army
army = pd.DataFrame(raw_data, columns=raw_data.keys())

# Set the 'origin' column as index
army = army.set_index('origin')

# Print the column veterans
print(army.veterans)

# Print veterans and deaths
print(army[['veterans', 'deaths']])

# Print the name of all columns
army.columns

# Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
states = ['Maine', 'Alaska']
army[army.index.isin(states)][['size', 'deserters']]

# Select the rows 3 to 7 and the columns 3 to 6
army.iloc[3:7, 3:6]

# Select every row after the fourth row and all columns
army.iloc[4:, :]

# Select every row up to the 4th row and all columns
army.iloc[:4, :]

# Select the 3rd column up to the 7th column
army.iloc[:, 3:7]

# Select rows where df.deaths is greater than 50
army[army.deaths > 50]

# Select rows where df.deaths is greater than 500 or less than 50
army[(army.deaths < 50) | (army.deaths > 500)]

# Select all the regiments not named "Dragoons"
army[~(army.regiment == 'Dragoons')]

# Select the rows called Texas and Arizona
army[army.index.isin(['Texas', 'California'])]

# Select the third cell in the row named Arizona
army[army.index == 'Arizona'].iloc[:, 3]

# Select the third cell down in the column named deaths
army['deaths'][3]

