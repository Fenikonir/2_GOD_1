from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Авторизация")
        Form.resize(218, 139)
        Form.setWindowIcon(QtGui.QIcon("handler/login.png"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_login = QtWidgets.QLineEdit(Form)
        self.le_login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.le_login.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.le_login)
        self.le_password = QtWidgets.QLineEdit(Form)
        self.le_password.setObjectName("lineEdit_2")
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.le_password)
        self.pb_login = QtWidgets.QPushButton(Form)
        self.pb_login.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pb_login)
        self.pb_registr = QtWidgets.QPushButton(Form)
        self.pb_registr.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pb_registr)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.le_login.setPlaceholderText(_translate("Form", "Логин"))
        self.le_password.setPlaceholderText(_translate("Form", "Пароль"))
        self.pb_login.setText(_translate("Form", "Войти"))
        self.pb_registr.setText(_translate("Form", "Регистрация"))