import sqlite3


def get_result(name):
    contacts = sqlite3.connect(name)
    cur = contacts.cursor()
    cur.execute("""UPDATE films
    SET duration = '42'
    WHERE duration = ''""")
    contacts.commit()

