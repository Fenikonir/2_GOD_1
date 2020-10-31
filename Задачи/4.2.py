import sqlite3
db2 = input()
conntact = sqlite3.connect(db2)
cur = conntact.cursor()
result = cur.execute("""SELECT * FROM Films
    WHERE title like 'Х%'""").fetchall()
a = set()
for elem in result:
    a.add(elem[2])
for i in range(len(a)):
    s = a.pop()
    print(s)
conntact.close()
