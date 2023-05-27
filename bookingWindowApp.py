import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from BookingWindow import Ui_BookingPage


class bookingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_BookingPage()
        self.ui.setupUi(self)



