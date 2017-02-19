import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('CREATE TABLE movies (name TEXT, year INTEGER, genre TEXT, freshness INTEGER)')
print("The table is live!")
connection.close()
