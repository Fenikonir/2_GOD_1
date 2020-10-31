import sqlite3


def get_result(name):
    contacts = sqlite3.connect(name)
    cur = contacts.cursor()
    cur.execute("""DELETE FROM films WHERE title like 'Я%а'""")
    contacts.commit()
