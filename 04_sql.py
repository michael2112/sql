import sqlite3
import csv

with sqlite3.connect("new.db") as conn:
	cursor = conn.cursor()

	employees = csv.reader(open("employees.csv", "rU"))

	cursor.execute('CREATE TABLE employees(firstname TEXT, lastname TEXT)')

	cursor.executemany(
		'INSERT INTO employees VALUES(?,?)', employees
		)
