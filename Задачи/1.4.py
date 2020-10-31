import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 255, 50)
        self.setWindowTitle('Арифмометр')

        self.name_input = QLineEdit(self)
        self.name_input.move(10, 10)
        self.name_input.resize(45, 30)

        self.name1_input = QLineEdit(self)
        self.name1_input.move(150, 10)
        self.name1_input.resize(45, 30)

        self.label = QLabel(self)
        self.label.setText("=")
        self.label.move(195, 16)

        self.name2_input = QLineEdit(self)
        self.name2_input.move(200, 10)
        self.name2_input.resize(45, 30)
        self.name2_input.setReadOnly(True)




        self.btn1 = QPushButton('+', self)
        self.btn1.resize(30, 30)
        self.btn1.move(56, 10)
        self.btn1.clicked.connect(self.plus)

        self.btn2 = QPushButton('-', self)
        self.btn2.resize(30, 30)
        self.btn2.move(87, 10)
        self.btn2.clicked.connect(self.minus)

        self.btn3 = QPushButton('*', self)
        self.btn3.resize(30, 30)
        self.btn3.move(118, 10)
        self.btn3.clicked.connect(self.proizv)








    def plus(self):
        x = int(self.name_input.text())
        y = int(self.name1_input.text())
        self.name2_input.setText(str(x+y))

    def minus(self):
        x = int(self.name_input.text())
        y = int(self.name1_input.text())
        self.name2_input.setText(str(x-y))

    def proizv(self):
        x = int(self.name_input.text())
        y = int(self.name1_input.text())
        self.name2_input.setText(str(x*y))







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # sys.exit(app.exec())
    app.exec()
