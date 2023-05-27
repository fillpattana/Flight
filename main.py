from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from BookingWindow import Ui_BookingPage
from PurchaseWindow import Ui_PurchasePage
from RegisterWindow import Ui_RegisterPage
from LoginWindow import Ui_LoginPage
from HistoryWindow import Ui_HistoryPage
from BookingWindow import Ui_BookingPage


class Ui_loginPage(QMainWindow):
    def changeToRegister(self):
        widget.setCurrentWidget(registerPage)


class Ui_registerPage(QMainWindow):
    pass


class Ui_bookingPage(QMainWindow):
    pass


class Ui_paymentPage(QMainWindow):
    pass


class Ui_buyTicketPage(QMainWindow):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    loginPage = QMainWindow()
    w1 = Ui_LoginPage()
    w1.setupUi(loginPage)
    widget.addWidget(loginPage)

    registerPage = QMainWindow()
    w2 = Ui_RegisterPage()
    w2.setupUi(registerPage)
    widget.addWidget(registerPage)


    widget.setCurrentWidget(loginPage)

    widget.setFixedHeight(700)
    widget.setFixedWidth(700)
    widget.show()
    app.exec_()



