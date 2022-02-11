

# Importing libraries
import pandas_datareader.data as reader
import datetime as dt

# Time periods
end = dt.datetime.now()
start = dt.datetime(year=2022, month=1, day=1)

# Bitcoin data
btc_usd_data = reader.get_data_yahoo('BTC-USD', start, end)

# The data we want to keep is "Open" and "Close" price
btc_usd_data = btc_usd_data[['Open', 'Close']]

# Importing sqlite3
import sqlite3

# Connection and cursor
connection = sqlite3.connect('stock_database.db')
cursor = connection.cursor()

# Loading data into Database
btc_usd_data.to_sql(
    'btc_usd',
    connection,
    if_exists='replace',
    index=True)



    
    
    


