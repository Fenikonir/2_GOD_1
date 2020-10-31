import random

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 320, 50)
        self.setWindowTitle('Вычисление выражений')

        self.name1_input = QLineEdit(self)
        self.name1_input.move(80, 16)
        self.name1_input.resize(200, 28)

        self.btn = QPushButton('Получить', self)
        self.btn.resize(70, 28)
        self.btn.move(5, 14)

        self.btn.clicked.connect(self.reading)

    def reading(self):
        lines = open("lines.txt", "rt", encoding="utf8").read().splitlines()
        if len(lines) != 0:
            self.name1_input.setText((random.choice(lines)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # sys.exit(app.exec())
    app.exec()
