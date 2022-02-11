import urllib.request
from PIL import Image
from utils import *
import pandas as pd
import sqlite3

"""
# IMAGE url: https://i.ibb.co/BrS6QBj/wde.png
URL = 'https://i.ibb.co/BrS6QBj/wde.png'
with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())
img = Image.open('temp.jpg')
"""


# Getting data from Google API
client_data, email_data = get_data()

# DataFrames
clients = get_dataframe(client_data)
emails = get_dataframe(email_data)

# Making numeric columns numeric
clients['Cliente'] = pd.to_numeric(clients['Cliente'])
emails['Tipo cliente'] = pd.to_numeric(emails['Tipo cliente'])
emails['Alta nueva'] = pd.to_numeric(emails['Alta nueva'])

def main():
    # Connection to database
    connection = sqlite3.connect('customers.db')
    cursor = connection.cursor()


    # 1. Query to create customer_info table
    q = """
    CREATE TABLE IF NOT EXISTS customer_info ( 
        customer_name VARCHAR(255) NOT NULL, 
        customer_mail VARCHAR(255) NOT NULL, 
        customer_cluster INTEGER NOT NULL, 
        is_customer BIT NOT NULL
    );
    """
    # Creating table
    create_or_insert(q, cursor, connection)

    # 2. Evaluating if the customer is in the database
    q = """SELECT * FROM customer_info;"""
    current_customers = sql_query(q, cursor)['customer_name'].values

    customer_names = list(clients['Nombre cliente'].values)

    for client in customer_names:
        if client not in current_customers:
            # Getting welcome message where customer is "Alta nueva"
            customer_cluster = clients[clients['Nombre cliente'] == client]['Cliente'].values[0]
            message_to_send = emails[(emails['Alta nueva'] == 1) & (emails['Tipo cliente'] == customer_cluster)]['Mensaje'].values[0]
            message_to_send = message_to_send.replace('NOMBRE_CLIENTE', client)
            # Getting e-mail address and sending message
            email_address = clients[clients['Nombre cliente'] == client]['Mail'].values[0]
            send_mail(email_address, message_to_send, 'Descuentos exclusivos!')
            # Now the client is not "Alta nueva". Storing the data in our database
            customer_values = list(clients[clients['Nombre cliente'] == client].values[0])
            customer_values.append(1)
            customer_values = tuple(customer_values)
            insert_query = f"INSERT INTO customer_info VALUES {customer_values};"
            create_or_insert(insert_query, cursor, connection)
            print('Cliente dado de alta')
        else:
            # Getting current customer message
            customer_cluster = clients[clients['Nombre cliente'] == client]['Cliente'].values[0]
            message_to_send = emails[(emails['Alta nueva'] == 0) & (emails['Tipo cliente'] == customer_cluster)]['Mensaje'].values[0]
            message_to_send = message_to_send.replace('NOMBRE_CLIENTE', client)
            # Getting e-mail address and sending message
            email_address = clients[clients['Nombre cliente'] == client]['Mail'].values[0]
            send_mail(email_address, message_to_send, f'{client}, tenemos descuentos para ti')
            print('Email enviado a nuestro cliente')


if __name__ == "__main__":
    main()