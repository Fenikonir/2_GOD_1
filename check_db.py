from PyQt5 import QtCore
from db_handler import *


class ProverThread(QtCore.QThread):
    marginal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        login(name, passw, self.marginal)

    def thr_register(self, name, passw):
        register(name, passw, self.marginal)

