from PurchaseWindow import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class purchasedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PurchasePage()
        self.ui.setupUi(self)

    def parameter(self, destination, departure, ticketType, date):
        pass