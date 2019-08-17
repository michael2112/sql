import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""
        SELECT population.city
            , population.population
            , regions.region 
        FROM population, regions
        WHERE population.city = regions.city
        """)

    c.execute("SELECT * FROM regions ORDER BY region ASC")

    rows = c.fetchall()

    for r in rows:
        print(r)