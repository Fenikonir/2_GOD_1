import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Вычисление выражений')

        self.name_input = QLineEdit(self)
        self.name_input.move(15, 50)

        self.name1_input = QLineEdit(self)
        self.name1_input.move(15, 200)


        self.btn = QPushButton('->', self)
        self.btn.resize(100, 30)
        self.btn.move(150, 125)

        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Первое число(целое):")
        self.label.move(15, 15)

        self.label2 = QLabel(self)
        self.label2.setText("Второе число(целое):")
        self.label2.move(15, 165)

        self.label3 = QLabel(self)
        self.label3.setText("Сумма:")
        self.label3.move(300, 20)
        self.LCD_count1 = QLCDNumber(self)
        self.LCD_count1.move(351, 20)

        self.label4 = QLabel(self)
        self.label4.setText("Разность:")
        self.label4.move(290, 90)
        self.LCD_count2 = QLCDNumber(self)
        self.LCD_count2.move(351, 90)

        self.label5 = QLabel(self)
        self.label5.setText("Произведение:")
        self.label5.move(267, 160)
        self.LCD_count3 = QLCDNumber(self)
        self.LCD_count3.move(351, 160)

        self.label6 = QLabel(self)
        self.label6.setText("Частное:")
        self.label6.move(300, 210)
        self.LCD_count4 = QLCDNumber(self)
        self.LCD_count4.move(351, 210)


    def hello(self):
        x = int(self.name_input.text())
        y = int(self.name1_input.text())
        self.LCD_count1.display(x + y)
        self.LCD_count2.display(x - y)
        self.LCD_count3.display(x * y)
        if y != 0:
            self.LCD_count4.display(x / y)
        else:
            self.LCD_count4.display("Error")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    # sys.exit(app.exec())
    app.exec()
