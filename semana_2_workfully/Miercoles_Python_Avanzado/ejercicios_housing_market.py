

import pandas as pd
import numpy as np

'''
Introduction:
This time we will create our own dataset with fictional numbers to describe house market. 
As we are going to create random data don't try to reason of the numbers
'''

# Step 2. Create 3 differents Series, each of length 100, as follows:
# 1. The first a random number from 1 to 4
# 2. The second a random number from 1 to 3
# 3. The third a random number from 10,000 to 30,000
serie1 = pd.Series(np.random.randint(1, 4, 100), name='serie1')
serie2 = pd.Series(np.random.randint(1, 3, 100), name='serie2')
serie3 = pd.Series(np.random.randint(10000, 30000, 100), name='serie3')

# Step 3. Let's create a DataFrame by joinning the Series by column
df = pd.concat([serie1, serie2, serie3], axis=1)

# Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']

# Step 5. Create a column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'
bigcolumn = pd.concat([serie1, serie2, serie3], axis=0)

# Step 6. Oops, it seems it is going only until index 99. Is it true?
'''Yes it is'''

# Step 7. Reindex the DataFrame so it goes from 0 to 299
bigcolumn = bigcolumn.reset_index(drop=True)



