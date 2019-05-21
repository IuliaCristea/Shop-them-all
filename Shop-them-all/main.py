import sqlite3

# connecting to the database
connection = sqlite3.connect("myTable.db")

# cursor
crsr = connection.cursor()

# SQL command to insert the data in the table
sql_command = """INSERT INTO User VALUES ("Rishabh");"""
crsr.execute(sql_command)