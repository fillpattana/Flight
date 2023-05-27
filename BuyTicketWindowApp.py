import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from BuyTicketWindow import Ui_BuyWindow


class BuyTicketWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_BuyWindow()
        self.ui.setupUi(self)


