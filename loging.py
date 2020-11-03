import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from check_db import *
from des import *
from tester import *


class Authorization(QtWidgets.QWidget):
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

    def close_aus(self):
        global ex_test
        ex_test = Testered()
        ex_test.show()
        ex_auth.close()


    def signal_handler(self, value):
        if_log_in = False
        infoBox = QtWidgets.QMessageBox()  ##Message Box that doesn't run
        infoBox.setWindowIcon(QtGui.QIcon("infoBox.png"))
        if value == "Неверный логин или пароль!":
            infoBox.setIcon(QtWidgets.QMessageBox.Critical)
        elif value == "Авторизация прошла успешно!":
            infoBox.setIcon(QtWidgets.QMessageBox.Information)
            if_log_in = True
        elif value == "Пользователь уже зарегестрирован":
            infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        else:
            infoBox.setIcon(QtWidgets.QMessageBox.Information)
        infoBox.setText("\n" + value)
        infoBox.setWindowTitle("Оповещение")
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close)
        infoBox.exec_()
        if if_log_in:
            self.close_aus()

    @prover_input
    def auth(self):
        name = self.ui.le_login.text()
        password = self.ui.le_password.text()
        self.check_db.thr_login(name, password)
        self.log_auth = name

    @prover_input
    def regin(self):
        name = self.ui.le_login.text()
        password = self.ui.le_password.text()
        self.check_db.thr_register(name, password)

    def user_info(self):
        con = sqlite3.connect("handler/users.db")
        cur = con.cursor()
        self.result = cur.execute("""SELECT * FROM Users WHERE login=?""", (self.log_auth,)).fetchall()[0]
        cur.close()
        con.close()


class Testered(QtWidgets.QWidget, Ui_Tester):
    def __init__(self, parent=None):
        super(Testered, self).__init__(parent)
        self.setupUi(self)
        self.Vibor.clicked.connect(self.start_test)
        self.Sleduch.clicked.connect(self.sled)
        self.Predidush.clicked.connect(self.pred)

    def start_test(self):
        self.quest_num = 0
        self.comboBox.setEnabled(False)
        self.Vibor.setEnabled(False)
        self.QuestLabel.setVisible(True)
        self.Predidush.setVisible(True)
        self.Sleduch.setVisible(True)
        self.Zaverchit.setVisible(True)
        self.set_quest()

    def set_quest(self):
        x = self.quest_num
        test = self.comboBox.currentText()
        questions = db_test_handler.get_guests(test)
        self.QuestLabel.setText(questions[x][2])
        if x == 0:
            self.Predidush.setEnabled(False)
        else:
            self.Predidush.setEnabled(True)
        if x == len(questions) - 1:
            self.Sleduch.setEnabled(False)
        else:
            self.Sleduch.setEnabled(True)

        answers = db_test_handler.get_answer(questions[x][2])
        self.radioButton_1.setText(answers[0][2])
        self.radioButton_1.setVisible(True)
        if len(answers) >= 2:
            self.radioButton_2.setText(answers[1][2])
            self.radioButton_2.setVisible(True)
        if len(answers) >= 3:
            self.radioButton_3.setText(answers[2][2])
            self.radioButton_3.setVisible(True)
        if len(answers) >= 4:
            self.radioButton_4.setText(answers[3][2])
            self.radioButton_4.setVisible(True)
        if len(answers) == 5:
            self.radioButton_5.setText(answers[4][2])
            self.radioButton_5.setVisible(True)




    def pred(self):
        self.quest_num -= 1
        self.radioButton_1.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.radioButton_5.setVisible(False)
        self.set_quest()

    def sled(self):
        self.quest_num += 1
        self.radioButton_1.setVisible(False)
        self.radioButton_2.setVisible(False)
        self.radioButton_3.setVisible(False)
        self.radioButton_4.setVisible(False)
        self.radioButton_5.setVisible(False)
        self.set_quest()










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex_auth = Authorization()
    ex_auth.show()

    sys.exit(app.exec_())
