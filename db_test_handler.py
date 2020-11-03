import sqlite3


# Добавление, Проверка и Авторизация
def get_tests():
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM tests ORDER BY NAME""").fetchall()
    cur.close()
    con.close()
    return result

def get_guests(tests):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM questions WHERE test=(
    SELECT id FROM tests
        WHERE name =?)""", (tests,)).fetchall()
    cur.close()
    con.close()
    return result

def get_answer(quest):
    con = sqlite3.connect("handler/tests.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM answer WHERE question=(
    SELECT id FROM questions
        WHERE question =?)""", (quest,)).fetchall()
    cur.close()
    con.close()
    return result

