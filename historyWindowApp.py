from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from HistoryWindow import *

class historyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HistoryPage()
        self.ui.setupUi(self)

    def showBookings(self, user):
        for tickets in user.getTicket():
            self.ui.BookingsLabel.setText(tickets.__str__())
