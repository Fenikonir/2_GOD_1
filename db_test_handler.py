import sqlite3


# Добавление, Проверка и Авторизация
def get_tests():
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tests ORDER BY NAME""").fetchall()
    cur.close()
    con.close()
    return result


get_tests()



