import pandas as pd
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import smtplib
from email.mime.text import MIMEText

def send_mail(to, message, subject, company_email_address='store@workfully.es'):
    """Send an e-mail to the provided address

    Params:
        - to: str, destinatary e-mail address
        - message: str, message to send
        - subject: str, the e-mail subject
        - company_email_address: str, default:'store@workfully.es', our company email
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = company_email_address
    msg['To'] = to
    # msg.attach(img)

    s = smtplib.SMTP('localhost')
    s.sendmail(company_email_address, [to], msg.as_string())
    s.quit()


def get_dataframe(data):
    """Returns cleaned DataFrame from a given list"""
    df = pd.DataFrame(data)
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    return df

def get_data(clients=True, emails=True):
    """Get data from Google API

    Params:
        - clients: bool, default True, whether the function returns client data or not
        - emails: bool, default True, whether the function returns e-mails data or not

    Returns:
        - client_values or email_values: list, client and e-mail data based on parameters.
    """

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # The ID and range of the spreadsheet
    SPREADSHEET_ID_1 = '12rowPjQXWy_TNms7uAqfaMBy0dyjR_CFg6gq_u4V7tY'
    SPREADSHEET_ID_2 = '1JEouLKLB-quLhWYmawsVNgs3mMYGwjJojoJ77RDkGgM'
    RANGE_NAME = 'Hoja 1!A:C'

    # Get credentials from the token file
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    # Client data
    if clients:
        client_results = sheet.values().get(spreadsheetId=SPREADSHEET_ID_1, range=RANGE_NAME).execute()
        client_values = client_results.get('values', [])
    # Email data
    if emails:
        email_results = sheet.values().get(spreadsheetId=SPREADSHEET_ID_2, range=RANGE_NAME).execute()
        email_values = email_results.get('values', [])

    # The data returned is list-type
    if clients and emails:
        return client_values, email_values
    elif emails:
        return email_values
    elif clients:
        return client_values

def sql_query(query, cursor):
    """Execute a SQL query and return a Pandas DataFrame
    with the obtained data.

    Params:
        - query: str, SQL query
        - cursor: sqlite3 cursor object
    """
    # Execute and store the query
    cursor.execute(query)
    ans = cursor.fetchall()

    # Table names
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(ans,columns=names)

def create_or_insert(query, cursor, connection):
    """Execute and commit a SQL query"""
    cursor.execute(query)
    connection.commit()
