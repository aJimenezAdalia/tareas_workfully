

import pandas as pd

# Import dataset
address = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

# Variable chipo
chipo = pd.read_csv(address, sep='\t')

# Max valued products

'''The prices are string, we need to clean them'''
chipo.item_price = pd.to_numeric(chipo.item_price.str[1:])
chipo.sort_values('item_price', ascending=False)['item_name'].head()

# Products that cost more than $10
chipo[chipo.item_price > 10].shape[0]

# Price of each item
chipo[['item_name', 'item_price']]

# Sort by the item name
chipo.sort_values('item_name')

# Qty of the most expensive item ordered
# way 1:
chipo.sort_values('item_price', ascending=False).head(1)['quantity'].values[0]
# way 2:
chipo[chipo.item_price == chipo.item_price.max()]['quantity'].values[0]

# Times was a Veggie Salad Bowl ordered
chipo[chipo.item_name == 'Veggie Salad Bowl']['quantity'].sum()

# How many times did someone order more than one Canned Soda
chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)].shape[0]