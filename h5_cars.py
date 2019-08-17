import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

#   c.execute("""
#        CREATE TABLE orders
#        (make TEXT, model TEXT, order_date DATE)
#        """)

    orders = [
        ('Ford', 'F150', '2019-01-01'),
        ('Ford', 'Escort', '2019-01-01'),
        ('Ford', 'Explorer', '2019-01-01'),
        ('Honda', 'Accord', '2019-01-01'),
        ('Honda', 'Pilot', '2019-01-01'),
        ('Ford', 'F150', '2019-01-02'),
        ('Ford', 'Escort', '2019-01-02'),
        ('Ford', 'Explorer', '2019-01-02'),
        ('Honda', 'Accord', '2019-01-02'),
        ('Honda', 'Pilot', '2019-01-02'),
        ('Ford', 'F150', '2019-01-03'),
        ('Ford', 'Escort', '2019-01-03'),
        ('Ford', 'Explorer', '2019-01-03'),
        ('Honda', 'Accord', '2019-01-03'),
        ('Honda', 'Pilot', '2019-01-03')
        ]

    print(orders)

    c.executemany("""
        INSERT INTO orders
        VALUES (?,?,?)
        """, orders)
