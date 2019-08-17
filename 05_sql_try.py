import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
    cursor.execute("""
    	        INSERT INTO populations
        	    VALUES ('New York City', 'NY', 8400000)
            	""")
    cursor.execute("""
                INSERT INTO populations
                VALUES ('San Francisco', 'CA', 8000000)
                """)
    conn.commit()

except sqlite3.OperationalError as oe:
    print("OperationalError! {}".format(oe))

conn.close()