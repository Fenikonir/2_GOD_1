import sys

from check_db import *
from des import *
from tester import *
import datetime as dt
import db_test_handler
import redactor


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
        ex_test = Testered(self.log_auth)
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
        self.log_auth = name
        password = self.ui.le_password.text()
        self.check_db.thr_login(name, password)

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
    def __init__(self, log_auth, parent=None):
        super(Testered, self).__init__(parent)
        self.log_auth = log_auth
        self.setupUi(self)
        self.Vibor.clicked.connect(self.start_test)
        self.Sleduch.clicked.connect(self.sled)
        self.Predidush.clicked.connect(self.pred)
        self.admin_rooted = admin_root(self.log_auth)
        if self.admin_rooted == "admin":
            self.Add_test.setVisible(True)
            self.Add_test.clicked.connect(self.add_test)

        _translate = QtCore.QCoreApplication.translate
        self.testss = {}
        result = db_test_handler.get_tests()
        for i in result:
            self.testss[i[1]] = i[0]
        for i in range(len(result)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, _translate("mainWindow", result[i][1]))

    def start_test(self):
        self.quest_num = 0
        self.its_answer = {}
        self.comboBox.setEnabled(False)
        self.Vibor.setEnabled(False)
        self.Add_test.setEnabled(False)
        self.QuestLabel.setVisible(True)
        self.Predidush.setVisible(True)
        self.Sleduch.setVisible(True)
        self.Zaverchit.setVisible(True)
        self.Zaverchit.clicked.connect(self.get_result)
        self.test = self.comboBox.currentText()
        self.questions_and_answers = db_test_handler.get_guests_and_answers(self.test)
        self.set_quest()

    def set_quest(self):
        x = self.quest_num
        questions = []
        for q in self.questions_and_answers:
            questions.append(q.question)
        self.quest = questions[x]
        self.QuestLabel.setText(self.quest)
        if x == 0:
            self.Predidush.setEnabled(False)
        else:
            self.Predidush.setEnabled(True)
        if x == len(questions) - 1:
            self.Sleduch.setEnabled(False)
        else:
            self.Sleduch.setEnabled(True)

        for q in self.questions_and_answers:
            if q.question == self.quest:
                i = -1
                for a in q.answers:
                    i += 1
                    self.radioButtons[i].setText(a.answer)
                    self.radioButtons[i].setVisible(True)
                    self.radioButtons[i].setChecked(a.checked)
                break

    def pred(self):
        self.quest_num -= 1
        self.get_rb()
        self.hide_rb()
        self.set_quest()

    def sled(self):
        self.quest_num += 1
        self.get_rb()
        self.hide_rb()
        self.set_quest()

    def hide_rb(self):
        for i in range(self.max_answers):
            self.radioButtons[i].setAutoExclusive(False)
            self.radioButtons[i].setChecked(False)
            self.radioButtons[i].repaint()
            self.radioButtons[i].setAutoExclusive(True)
            self.radioButtons[i].setVisible(False)

    def get_rb(self):
        for i in range(self.max_answers):
            self.story_Checked(i)

    def get_result(self):
        self.get_rb()
        question_correct = 0
        uncorrect_questions = []
        for q in self.questions_and_answers:
            correct = True
            for a in q.answers:
                if a.correct != str(a.checked):
                    correct = False
                    uncorrect_questions.append(q.question_id)
                    break
            if correct:
                question_correct += 1
        db_test_handler.uncorrect = uncorrect_questions

        result = "Всего вопросов: " + str(len(self.questions_and_answers)) + "\n"
        result_1 = "Правильных ответов: " + str(question_correct) + "\n"
        str(question_correct / len(self.questions_and_answers) * 100)
        db_test_handler.write_result(self.test, self.log_auth, dt.datetime.now(),
                                     len(self.questions_and_answers), question_correct)

        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Information)
        infoBox.setWindowIcon(QtGui.QIcon("infoBox.png"))
        infoBox.setText("\n" + result + result_1)
        infoBox.setWindowTitle("Результат")
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close)
        infoBox.exec_()
        self.restart()

    def story_Checked(self, i):
        for q in self.questions_and_answers:
            if q.question == self.quest:
                for a in q.answers:
                    if a.answer == self.radioButtons[i].text():
                        a.checked = self.radioButtons[i].isChecked()
                break

    def restart(self):
        global ex_test
        ex_test.close()
        ex_test = Testered(self.log_auth)
        ex_test.show()

    def add_test(self):
        global red
        red = Redactor()
        red.show()


class Redactor(QtWidgets.QWidget, redactor.Redactor):
    def __init__(self, parent=None):
        super(Redactor, self).__init__(parent)
        self.redactor_question = False
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.add_quest)

    def add_quest(self):
        test = self.lineEdit.text()
        question = self.lineEdit_2.text()
        check_test = self.check_test(test)
        a = self.check_quest(test, question)
        if a or self.redactor_question:
            answers = {}
            for i in range(5):
                if self.answers_line_edit[i].text() != "":
                    isCheked = self.answers_check_box[i].isChecked()
                    if isCheked:
                        isCheked = "True"
                    else:
                        isCheked = "False"
                    answers[i] = [self.answers_line_edit[i].text(), isCheked]
            if a:
                db_test_handler.write_quest(test, check_test, question, answers)
            if not a:
                db_test_handler.update_quest(test, check_test, question, answers)
            self.redactor_question = False
            self.signal_handler(True)
            self.lineEdit_2.clear()
            for i in range(5):
                self.answers_line_edit[i].clear()
                self.answers_check_box[i].setChecked(False)
        elif not a:
            self.signal_handler(False)
            for i in range(len(self.quested)):
                if self.quested[i].question == question:
                    x = 0
                    for j in self.quested[i].answers:
                        self.answers_line_edit[x].setText(j.answer)
                        if j.correct == "True":
                            self.answers_check_box[x].setChecked(True)
                        x += 1
                    self.redactor_question = True
                    break

    def check_test(self, test):
        tests = []
        for i in db_test_handler.get_tests():
            tests.append(i[1])
        if test in tests:
            return True
        else:
            return False

    def check_quest(self, test, quest):
        quests = []
        self.quested = db_test_handler.get_guests_and_answers(test)
        for q in self.quested:
            quests.append(q.question)
        if quest in quests:
            return False
        else:
            return True

    def signal_handler(self, valvs):
        infoBox = QtWidgets.QMessageBox()  ##Message Box that doesn't run
        infoBox.setWindowIcon(QtGui.QIcon("infoBox.png"))
        if not valvs:
            infoBox.setIcon(QtWidgets.QMessageBox.Warning)
            infoBox.setText("\n" + "Такой вопрос уже есть")
        else:
            infoBox.setIcon(QtWidgets.QMessageBox.Information)
            infoBox.setText("\n" + "Тест изменен")
        infoBox.setWindowTitle("Оповещение")
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close)
        infoBox.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex_auth = Authorization()
    ex_auth.show()

    sys.exit(app.exec_())
