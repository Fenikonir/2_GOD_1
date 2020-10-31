import sqlite3
db1 = input()
conntact = sqlite3.connect(db1)
cur = conntact.cursor()
result = cur.execute('''SELECT title FROM films WHERE genre IN (SELECT id FROM genres WHERE title IN
            ('музыка', 'анимация')) and year >= 1997''').fetchall()
for elem in result:
    print(elem[0])
conntact.close()