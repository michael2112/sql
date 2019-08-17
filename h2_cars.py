import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
            ('Ford', 'F150', 600000),
            ('Ford', 'Escort', 2700000),
            ('Ford', 'Explorer', 2100000),
            ('Honda', 'Accord', 1500000),
            ('Honda', 'Pilot', 1500000)
            ]

    c.executemany("""
        INSERT INTO inventory
        VALUES (?,?,?)
        """, cars)
