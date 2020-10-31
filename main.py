import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from check_db import *
from des import *


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pb_registr.clicked.connect(self.regin)
        self.ui.pb_login.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.le_login, self.ui.le_password]

        self.check_db = ProverThread()
        self.check_db.marginal.connect(self.signal_handler)


    def prover_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def signal_handler(self, value):
        infoBox = QtWidgets.QMessageBox()  ##Message Box that doesn't run
        if value == "Неверный логин или пароль!":
            infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        else:
            infoBox.setIcon(QtWidgets.QMessageBox.Information)
        infoBox.setText("\n" + value)
        infoBox.setWindowTitle("Оповещение")
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close)
        infoBox.exec_()

    @prover_input
    def auth(self):
        name = self.ui.le_login.text()
        password = self.ui.le_password.text()
        self.check_db.thr_login(name, password)

    @prover_input
    def regin(self):
        name = self.ui.le_login.text()
        password = self.ui.le_password.text()
        self.check_db.thr_register(name, password)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())




