import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from BuyTicketWindow import Ui_BuyWindow
from LoginFunc import *


class BuyTicketWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_BuyWindow()
        self.ui.setupUi(self)

    def Popup(self):
        popup = QErrorMessage()
        popup.showMessage("Insufficient Amount of Money")
        popup.exec_()

    def showSelectedTicket(self, ticket):
        qm = QMessageBox()
        text = "YOUR TICKET\n\n" + ticket.__str__()
        qm.setWindowTitle("Confirm Purchase")
        qm.setText(text)
        qm.setStandardButtons(QMessageBox.StandardButton.Yes)
        x = qm.exec_()



