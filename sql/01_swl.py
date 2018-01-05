"""
STEPS:
1- Create a database connection
2- Get a cursor
3- Execute your SQL query
4- Close the connection
"""

import sqlite3

#create a new database if doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commnands
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE population
              (city TEXT, state TEXT, population INT)""")

#close database connection
conn.close()
