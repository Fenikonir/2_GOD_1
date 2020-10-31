import sqlite3


# Добавление, Проверка и Авторизация
def login(login, password, signal):
    con = sqlite3.connect("handler/users.db")
    cur = con.cursor()

    result = cur.execute("""SELECT * FROM Users WHERE login=?""", (login,)).fetchall()

    if result != [] and result[0][2] == password:
        signal.emit("Авторизация прошла успешно!")
    else:
        signal.emit("Неверный логин или пароль!")

    cur.close()
    con.close()
