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
        self.its_answer = {}
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
        self.quest = questions[x][2]
        self.QuestLabel.setText(questions[x][2])
        if x == 0:
            self.Predidush.setEnabled(False)
        else:
            self.Predidush.setEnabled(True)
        if x == len(questions) - 1:
            self.Sleduch.setEnabled(False)
        else:
            self.Sleduch.setEnabled(True)

        self.answers = db_test_handler.get_answer(questions[x][2])
        self.radioButton_1.setText(self.answers[0][2])
        self.radioButton_1.setVisible(True)
        self.radioButton_1.toggled.connect(lambda: self.clik_radio(1))
        self.rb1 = self.answers[0]
        if len(self.answers) >= 2:
            self.radioButton_2.setText(self.answers[1][2])
            self.radioButton_2.setVisible(True)
            self.radioButton_2.toggled.connect(lambda: self.clik_radio(2))
            self.rb2 = self.answers[1]
        if len(self.answers) >= 3:
            self.radioButton_3.setText(self.answers[2][2])
            self.radioButton_3.setVisible(True)
            self.radioButton_3.toggled.connect(lambda: self.clik_radio(3))
            self.rb3 = self.answers[2]
        if len(self.answers) >= 4:
            self.radioButton_4.setText(self.answers[3][2])
            self.radioButton_4.setVisible(True)
            self.radioButton_4.toggled.connect(lambda: self.clik_radio(4))
            self.rb4 = self.answers[3]
        if len(self.answers) == 5:
            self.radioButton_5.setText(self.answers[4][2])
            self.radioButton_5.setVisible(True)
            self.radioButton_5.toggled.connect(lambda: self.clik_radio(5))
            self.rb5 = self.answers[4]
        if self.quest in self.its_answer:
            if self.its_answer[self.quest] == 1:
                self.radioButton_1.setChecked(True)
            if self.its_answer[self.quest] == 2:
                self.radioButton_2.setChecked(True)
            if self.its_answer[self.quest] == 3:
                self.radioButton_3.setChecked(True)
            if self.its_answer[self.quest] == 4:
                self.radioButton_4.setChecked(True)
            if self.its_answer[self.quest] == 5:
                self.radioButton_5.setChecked(True)


    def pred(self):
        self.quest_num -= 1
        for btn in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4, self.radioButton_5]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.setVisible(False)
        self.set_quest()

    def sled(self):
        self.quest_num += 1
        for btn in [self.radioButton_1, self.radioButton_2, self.radioButton_3, self.radioButton_4, self.radioButton_5]:
            btn.setAutoExclusive(False)
            btn.setChecked(False)
            btn.repaint()
            btn.setAutoExclusive(True)
            btn.setVisible(False)
        self.set_quest()

    def clik_radio(self, x):
        self.its_answer[self.quest] = x





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex_auth = Authorization()
    ex_auth.show()

    sys.exit(app.exec_())
