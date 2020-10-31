import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = False
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.btn1.clicked.connect(lambda: self.run("1"))
        self.btn2.clicked.connect(lambda: self.run("2"))
        self.btn3.clicked.connect(lambda: self.run("3"))
        self.btn4.clicked.connect(lambda: self.run("4"))
        self.btn5.clicked.connect(lambda: self.run("5"))
        self.btn6.clicked.connect(lambda: self.run("6"))
        self.btn7.clicked.connect(lambda: self.run("7"))
        self.btn8.clicked.connect(lambda: self.run("8"))
        self.btn9.clicked.connect(lambda: self.run("9"))
        self.btn0.clicked.connect(lambda: self.run("0"))

        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self, x):
        if not self.c:
            self.table.display(x)
        else:
            self.c = True
            y = self.table.text()
            self.table.display(x + y)

        # Имя элемента совпадает с objectName в QTDesigner

    def run_1(self):
        self.tabel.display(2)

    def run_3(self):
        None

    def run_4(self):
        None

    def run_5(self):
        None

    def run_6(self):
        None

    def run_7(self):
        None

    def run_8(self):
        None

    def run_9(self):
        None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())