from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from BookingWindow import Ui_BookingPage
from PurchaseWindow import Ui_PurchasePage
from RegisterWindow import Ui_RegisterPage
from LoginWindow import Ui_LoginPage
from HistoryWindow import Ui_HistoryPage


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self.main_win)



    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())


