import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import sqlite3
db2 = input()
conntact = sqlite3.connect(db2)
cur = conntact.cursor()
result = cur.execute("""SELECT * FROM Films 
    WHERE genre=(
SELECT id FROM genres 
    WHERE title = 'комедия') and duration >= 60""").fetchall()
for elem in result:
    print(elem[1])

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('flag.ui', self)  # Загружаем дизайн


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())