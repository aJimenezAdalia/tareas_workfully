
# 1
import pandas as pd
import numpy as np

# 2
address = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
pd.read_csv(address, sep='|')

# 3.
users = pd.read_csv(address, sep='|').set_index('user_id')

# 4.

# Way 1:
print(users.head(25))
# Way 2:
print(users.iloc[:25])

# 5.
print(users.tail(10))

# 6.

# Way 1.
print(users.shape[0] * users.shape[1])
# Way 2.
print(len(users.index) * len(users.columns))

# 7.

# Way 1.
print(len(users.columns))
# Way 2.
print(users.shape[1])

# 8.
print(users.columns)

# 9.
print(users.index.values)

# 10.

# Way 1.
for column in users.columns:
  print(column, users[column].dtype)
# Way 2.
print(users.dtypes)

# 11.

# Way 1.
print(users.occupation)
# Way 2.
print(users.loc[:, 'occupation'])

# 12.

# Different occupations:
users.occupation.unique()
# Users per occupation
users.occupation.value_counts()

# 13.
users.occupation.value_counts().head(1).index.values[0]

# 14.
users.describe()

# 15
users.info()

# 16
users.occupation.describe()

# 17
users.age.mean()

# 18.
users.age.value_counts().tail(1)