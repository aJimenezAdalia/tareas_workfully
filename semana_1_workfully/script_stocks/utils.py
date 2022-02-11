
import pandas as pd

def sql_query(query, cursor):
    """Receive SQL by parameter, execute the
    query in a connected database, and return
    a Pandas DataFrame with the obtained data.

    Params:
        - query: str expected, SQL query
    Return:
        - pd.DataFrame, query data
    """

    cursor.execute(query)
    ans = cursor.fetchall()
    names = [description[0] for description in cursor.description]

    return pd.DataFrame(ans, columns=names)