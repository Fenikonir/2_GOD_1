import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox





class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.cb4 = QCheckBox('edit4', self)
        self.cb3 = QCheckBox('edit3', self)
        self.cb2 = QCheckBox('edit2', self)
        self.cb1 = QCheckBox('edit1', self)
        self.name1_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.name3_input = QLineEdit(self)
        self.name2_input = QLineEdit(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Прятки для виджетов')

        self.name_input.move(100, 10)
        self.name_input.resize(100, 20)
        self.name_input.setText("Поле edit1")

        self.name1_input.move(100, 30)
        self.name1_input.resize(100, 20)
        self.name1_input.setText("Поле edit2")

        self.name2_input.move(100, 50)
        self.name2_input.resize(100, 20)
        self.name2_input.setText("Поле edit3")

        self.name3_input.move(100, 70)
        self.name3_input.resize(100, 20)
        self.name3_input.setText("Поле edit4")

        self.cb1.move(20, 10)
        self.cb1.stateChanged.connect(self.hello(self.name_input, self.cb1))
        self.cb2.move(20, 30)
        self.cb2.stateChanged.connect(self.hello(self.name1_input, self.cb2))
        self.cb3.move(20, 50)
        self.cb3.stateChanged.connect(self.hello(self.name2_input, self.cb3))
        self.cb4.move(20, 70)
        self.cb4.stateChanged.connect(self.hello(self.name3_input, self.cb4))

    def hello(self, x, y):
        if y.isChecked():
            x.show()
        else:
            x.hide()

        # if self.cb1.isHidden():
        #     self.name_input1.hide()
        # # else:
        # #     self.name_input1.show()
        #
        # self.cb2 = QCheckBox('edit2', self)
        # self.cb3 = QCheckBox('edit3', self)
        # self.cb4 = QCheckBox('edit4', self)
        #
        # self.name_input1 = QLineEdit(self)
        # self.name_input2 = QLineEdit(self)
        # self.name_input3 = QLineEdit(self)
        # self.name_input4 = QLineEdit(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # sys.exit(app.exec())
    app.exec()
