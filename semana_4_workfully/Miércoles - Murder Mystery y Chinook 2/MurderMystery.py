

import sqlite3
import pandas as pd


# Function to get a DataFrame from a SQL Query
def sql_query(cursor, query):
    cursor.execute(query)
    ans = cursor.fetchall()
    names = [x[0] for x in cursor.description]

    return pd.DataFrame(ans, columns=names)


# Connecting to DataBase
database_path = '/Users/antoniojimenez/Desktop/Carpeta Alumno Workfully/4 - SQL/2 - Joins y subconsultas/Practica/sql-murder-mystery.db'

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

# Query 1 - Start
q = """
SELECT description, date
FROM crime_scene_report
WHERE date = 20180115
"""
q1 = sql_query(cursor, q)

'''
Two persons: 
    - 1. Lives at the last house on "Northwestern Dr"
    - 2. Named Annabel, lives somewhere on "Franklin Ave."
'''

# Query 2 - Person 1 Info
q = """
SELECT *
FROM person
WHERE name LIKE "Morty%";
"""
q2 = sql_query(cursor, q)

# Query 3 - Person 2 Info
q = """
SELECT *
FROM person
WHERE name LIKE "Annabel%";
"""
q3 = sql_query(cursor, q)

'''
- Person 1 
    - Name: Morty Schapiro
    - Person ID: 14887
    - Address: 4919 Northwestern Dr 
    - License ID: 118009
    - SSN: 111564949

- Person 2
    - Name: Annabel Miller
    - Person ID: 16371
    - Address: 103 Franklin Ave
    - License ID: 490173
    - SSN: 318771143
'''

# Query 4 - Information from Morty Schapiro
q = """
SELECT transcript
FROM interview
WHERE person_id = 14887;
"""
q4 = sql_query(cursor, q)

# Query 5 - Information from Annabel Miller
q = """
SELECT transcript
FROM interview
WHERE person_id = 16371;
"""
q5 = sql_query(cursor, q)


'''
    - Someone heard a gunshot, a man run out
    - He had a "Get Fit Now Gym" bag
    - Membership number on the bag started with "48Z" (Gold Member)
    - Car plate included "H42W"
    - The killer was in the gym on January 9th
'''

# Query 6 - Get Fit Now Gym Check-in, January 9th
q = """
SELECT *
FROM get_fit_now_check_in
WHERE (check_in_date = 20180109)
AND membership_id LIKE ('48Z%');
"""
q6 = sql_query(cursor, q)

'''
- Member 1: Membership ID 48Z7A; check-in: 16.00, check-out: 17.30
- Member 2: Membership ID 48Z55; check-in: 15.30, check-out: 17.00
'''

# Query 7 - Get Fit Now Members
q = """
SELECT *
FROM get_fit_now_member
WHERE membership_status = 'gold'
AND id IN ('48Z7A', '48Z55');
"""
q7 = sql_query(cursor, q)

'''
Suspect 1. 
    - Name: Jeremy Bowers 
    - Person ID: 67318
Suspect 2.
    - Name: Joe Germuska
    - Person ID: 28819
'''


# Query 8 - Facebook Event Checking - Jeremy Bowers
q = """
SELECT *
FROM facebook_event_checkin
WHERE person_id = 67318;
"""
q8 = sql_query(cursor, q)

# Query 9 - Facebook Event Checking - Joe Germuska
q = """
SELECT *
FROM facebook_event_checkin
WHERE person_id = 28819;
"""
q9 = sql_query(cursor, q)

'''
Jeremy Bowers January 15th:
    - The Funky Grooves Tour
Joe Germuska January 15th:
    - No information
'''

# Query 10 - Following Joe Germuska - Drivers License
q = """
SELECT *
FROM drivers_license
WHERE plate_number LIKE ('%H42W%');
"""
q10 = sql_query(cursor, q)

# Query 11 - Interview - Joe Germuska
q = """
SELECT *
FROM get_fit_now_member
WHERE person_id = 28819;
"""
q11 = sql_query(cursor, q)

'''
The Murder is Jeremy Bowers
'''


