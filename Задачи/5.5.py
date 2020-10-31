import sqlite3


def get_result(name):
    contacts = sqlite3.connect(name)
    cur = contacts.cursor()
    cur.execute("""UPDATE films
    SET duration = 100
    WHERE genre=(
    SELECT id FROM genres
        WHERE title = 'мюзикл') and duration > 100""")
    contacts.commit()
