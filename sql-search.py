import sqlite3

connection = sqlite3.connect("newnum.db")

c = connection.cursor()

prompt = """
Select the op that you want to perform [1-5]: 1. Average 2. Max 3. Min 4. Sum 5. Exit : """

while True:
    x = input(prompt)

    if x in ["1","2","3","4"]:
        op = {1: "AVG", 2: "MAX", 3: "MIN", 4: "SUM"}[int(x)]

        c.execute("SELECT {}(num) FROM numbers".format(op))

        get = c.fetchone()

        print(op + ": %f" % get[0])

    elif x == "5":
        print("Exit")
        break

    else:
        print("Not a choice. Try again...")