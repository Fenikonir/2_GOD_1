import sqlite3
db2 = input()
conntact = sqlite3.connect(db2)
cur = conntact.cursor()
result = cur.execute("""SELECT * FROM Films 
    WHERE year >= 2010 and year <= 2011""").fetchall()

a = set()
for elem in result:
    a.add(elem[3])
for i in range(len(a)):
    s = a.pop()
    res = cur.execute(f"""SELECT * FROM genres 
        WHERE id == {s}""").fetchall()
    print(res[0][1])
conntact.close()
