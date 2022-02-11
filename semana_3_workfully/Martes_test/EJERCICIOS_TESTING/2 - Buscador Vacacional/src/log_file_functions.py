

import pandas as pd

data = open('logging.log', 'r').read()

# Function 1
def filter_log_levels(log_file_path='logging.log', log_level='all'):
    """Builds a Pandas DataFrame with logging information,
    and returns the logs of the provided level by parameter.

    Params:
        - log_file_path: str, path where the file is stored
        - log_level: str, default:'INFO', log level

    Returns:
        - df: Pandas DataFrame, dataframe with the desired data
    """
    if log_level.upper() not in ['DEBUG', 'INFO', 'WARNING' 'ERROR', 'CRITICAL', 'ALL']:
        return print("Invalid Log Level.")

    log_level = log_level.upper()

    log_data = pd.read_csv(log_file_path,
                           sep='-',
                           names=['date', 'logger', 'log_level', 'event'])

    if log_level == 'ALL':
        return log_data
    else:
        df = log_data[log_data['log_level'] == log_level]
        return df


# Function 2
def filter_logs_by_timestamp(start_date, end_date, log_file_path='logging.log'):
    """Returns a Pandas DataFrame with logs info. The returned data
    is based on the received dates by parameter.

    Params:
        - start_date: str expected, initial date to select the data
        - end_date: str expected, end date to select the data
    Returns:
        - custom_period_data: Pandas DataFrame, the desired data
    """

    # Obtaining Pandas DataFrame
    df = filter_log_levels(log_file_path=log_file_path,
                           log_level='ALL')

    df['date'] = pd.to_datetime(df['date'])
    custom_period_data = df[(df['date'] > start_date) & (df['date'] < end_date)]

    return custom_period_data


# Function 3
def try_except_info(log_file_path='logging.log'):
    pass
    # ????

# Function 4
def log_filtering(log_file_path='logging.log', to_search=''):
    """Find a string inside a log file

    Params:
        - log_file_path: str, path to file
        - to_search: str, string to search
    """

    data = open(log_file_path, 'r').read()

    number_of_occurrences = data.count(to_search)

    if number_of_occurrences:
        return print(f"The are {number_of_occurrences} occurrences.")
    else:
        return print(f"The word {to_search} is not in the log file.")



