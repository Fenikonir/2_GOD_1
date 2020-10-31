import sqlite3
db2 = input()
conntact = sqlite3.connect(db2)
cur = conntact.cursor()
result = cur.execute("""SELECT * FROM Films
    WHERE title like '%Астерикс%' and title not like '%Обеликс%'""").fetchall()
for elem in result:
    print(elem[1])
conntact.close()