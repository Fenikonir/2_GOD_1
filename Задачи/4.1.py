import sqlite3
db2 = input()
conntact = sqlite3.connect(db2)
cur = conntact.cursor()
result = cur.execute("""SELECT * FROM films
            WHERE title LIKE '%?'""").fetchall()
for elem in result:
    print(elem[1])
conntact.close()