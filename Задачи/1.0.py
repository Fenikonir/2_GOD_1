import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = True
        self.setGeometry(300, 300, 320, 50)
        self.setWindowTitle('Вычисление выражений')

        self.name_input = QLineEdit(self)
        self.name_input.move(5, 14)

        self.name1_input = QLineEdit(self)
        self.name1_input.move(182, 14)


        self.btn = QPushButton('->', self)
        self.btn.resize(28, 28)
        self.btn.move(145, 11)

        self.btn.clicked.connect(self.hello)


    def hello(self):
        if self.col:
            name = self.name_input.text()
            # Получим текст из поля ввода
            self.name1_input.setText(name)
            self.name_input.clear()
            self.btn.setText("<-")
            self.col = False
        else:
            name = self.name1_input.text()
            # Получим текст из поля ввода
            self.name_input.setText(name)
            self.name1_input.clear()
            self.btn.setText("->")
            self.col = True




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # sys.exit(app.exec())
    app.exec()

