import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""
        UPDATE inventory
        SET quantity = 1111111
        WHERE make = 'Honda'
        """)

    c.execute("SELECT * FROM inventory")

    rows = c.fetchall()

    for r in rows:
        print(r)