from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

from LoginFunc import *

from bookingWindowApp import *
from registerWindowApp import *
from purchasedWindowApp import *
from LoginWindowApp import *
from BuyTicketWindowApp import *
from historyWindowApp import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    loginPage = LoginWindow()
    widget.addWidget(loginPage)

    registerPage = registerWindow()
    widget.addWidget(registerPage)

    bookingWindow = bookingWindow()
    widget.addWidget(bookingWindow)

    purchaseWindow = purchasedWindow()
    widget.addWidget(purchaseWindow)

    buyWindow = BuyTicketWindow()
    widget.addWidget(buyWindow)

    historyWindow = historyWindow()
    widget.addWidget(historyWindow)

    widget.setCurrentWidget(loginPage)

    widget.setFixedHeight(700)
    widget.setFixedWidth(750)
    widget.show()

    loginPage.ui.registerButton.clicked.connect(lambda : widget.setCurrentWidget(registerPage))

    registerPage.ui.goToLogin.clicked.connect(lambda : widget.setCurrentWidget(loginPage))
    registerPage.ui.gobacktologin.clicked.connect(lambda: widget.setCurrentWidget(loginPage))

    bookingWindow.ui.goToLogin.clicked.connect(lambda : widget.setCurrentWidget(loginPage))
    bookingWindow.ui.goToTicketSelect.clicked.connect(lambda : widget.setCurrentWidget(purchaseWindow))
    bookingWindow.ui.viewBookings.clicked.connect(lambda : widget.setCurrentWidget(historyWindow))

    purchaseWindow.ui.goBack.clicked.connect(lambda : widget.setCurrentWidget(bookingWindow))
    purchaseWindow.ui.goNext.clicked.connect(lambda : widget.setCurrentWidget(buyWindow))

    historyWindow.ui.goBack.clicked.connect(lambda : widget.setCurrentWidget(bookingWindow))


    def abcdee():
        desti = bookingWindow.ui.dropdown_destination.currentText()
        depart = bookingWindow.ui.dropdown_departure.currentText()
        tT = bookingWindow.ui.dropdow_tickettype.currentText()
        time = bookingWindow.ui.dateEdit.date()
        purchaseWindow.parameter(desti, depart, tT, time)
        widget.setCurrentWidget(purchaseWindow)

    bookingWindow.ui.GenerateTicks.clicked.connect(abcdee)

    def LoginToApp():
        username = loginPage.ui.username_input.text()
        password = loginPage.ui.password_input.text()
        LoginWindow().VerifyLogin(username, password)
        widget.setCurrentWidget(bookingWindow)

    loginPage.ui.loginButton.clicked.connect(LoginToApp)

# add user button
    def registerUser():
        name = registerPage.ui.regis_name_input.text()
        age = registerPage.ui.regis_age_input.text()
        username = registerPage.ui.regis_user_input.text()
        password = registerPage.ui.regis_pw_input.text()
        registerWindow.addNewUser(registerWindow(), username, password, name, age)

# print info
    def information():
        registerWindow.infos(registerWindow())

    registerPage.ui.addUser.clicked.connect(registerUser)
    registerPage.ui.addUser.clicked.connect(information)

# add a credit card
    def registerCredit():
        cpin = registerPage.ui.credit_pin.text()
        username = registerPage.ui.regis_user_input.text()
        name = registerPage.ui.regis_name_input.text()
        registerWindow.addCredit(registerWindow(), username, "creditCard", name, cpin)

    registerPage.ui.addCreditCard.clicked.connect(registerCredit)
    registerPage.ui.addCreditCard.clicked.connect(information)

# add a debit card
    def registerDebit():
        dpin = registerPage.ui.debit_pin.text()
        username = registerPage.ui.regis_user_input.text()
        name = registerPage.ui.regis_name_input.text()
        registerWindow.addDebit(registerWindow(), username, "debitCard", name, dpin)

    registerPage.ui.addDebitCard.clicked.connect(registerDebit)
    registerPage.ui.addDebitCard.clicked.connect(information)

#login to go to booking page

    app.exec_()



