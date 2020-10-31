from PyQt5 import QtCore, QtGui, QtWidgets
from handler.db_handler import *


class ProverThread(QtCore.QThread):
    marginal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.marginal)

    def thr_register(self, name, passw):
        register(name, passw, self.marginal)
