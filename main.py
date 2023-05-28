from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from bookingWindowApp import *
from registerWindowApp import *
from purchasedWindowApp import *
from LoginWindowApp import *
from BuyTicketWindowApp import *
from historyWindowApp import *

from flightTicket import *
from user import *

if __name__ == '__main__':
    ticketNow = ["1", "2", "3", "4", "5"]
    selectedTicket = flightTicket("", "", "", "", "", "", "", "")
    NowLoginCustomer = CreateUser("", "", "", "")
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

    purchaseWindow.ui.goBack.clicked.connect(lambda : widget.setCurrentWidget(bookingWindow))
    purchaseWindow.ui.goNext.clicked.connect(lambda : widget.setCurrentWidget(buyWindow))

    historyWindow.ui.goBack.clicked.connect(lambda : widget.setCurrentWidget(bookingWindow))


    def abcdee():
        desti = bookingWindow.ui.dropdown_destination.currentText()
        depart = bookingWindow.ui.dropdown_departure.currentText()
        tT = bookingWindow.ui.dropdow_tickettype.currentText()
        time = bookingWindow.ui.dateEdit.date()
        user = NowLoginCustomer
        global ticketNow
        ticketNow = purchaseWindow.parameter(desti, depart, tT, time, user)
        widget.setCurrentWidget(purchaseWindow)

    bookingWindow.ui.GenerateTicks.clicked.connect(abcdee)

    def payTicket1():
        tick = ticketNow[0]
        global selectedTicket
        selectedTicket = purchaseWindow.confirm(tick)
        widget.setCurrentWidget(buyWindow)

    def payTicket2():
        tick = ticketNow[1]
        global selectedTicket
        selectedTicket = purchaseWindow.confirm(tick)
        widget.setCurrentWidget(buyWindow)

    def payTicket3():
        tick = ticketNow[2]
        global selectedTicket
        selectedTicket = purchaseWindow.confirm(tick)
        widget.setCurrentWidget(buyWindow)

    def payTicket4():
        tick = ticketNow[3]
        global selectedTicket
        selectedTicket = purchaseWindow.confirm(tick)
        widget.setCurrentWidget(buyWindow)

    def payTicket5():
        tick = ticketNow[4]
        global selectedTicket
        selectedTicket = purchaseWindow.confirm(tick)
        widget.setCurrentWidget(buyWindow)


    purchaseWindow.ui.payTick1.clicked.connect(payTicket1)
    purchaseWindow.ui.payTick2.clicked.connect(payTicket2)
    purchaseWindow.ui.payTick3.clicked.connect(payTicket3)
    purchaseWindow.ui.payTick4.clicked.connect(payTicket4)
    purchaseWindow.ui.payTick5.clicked.connect(payTicket5)

    def buy():
        pin = buyWindow.ui.enterPin.text()
        buyPrice = selectedTicket.getPrice()
        user = NowLoginCustomer
        i = buyWindow.ui.selectCard.currentText()
        cards = get_user_attribute(user, "cards")
        t = get_user_attribute(user, "ticketBought")
        selectedcard = cards[int(i)-1]
        cardlim = selectedcard.getBalance()
        cardbal = selectedcard.getBalance()
        p = selectedcard.getPin()

        if isinstance(selectedcard, CreditCard) and cardlim > buyPrice and p == pin:
            price = cardlim - buyPrice
            update_pickle_user(user, price)
            t.append(selectedTicket)
            print(selectedTicket)
            buyWindow.showSelectedTicket(selectedTicket)
            print("Card Limit: ", selectedcard.getBalance())
            widget.setCurrentWidget(bookingWindow)
        elif isinstance(selectedcard, DebitCard) and cardbal > buyPrice and p == pin:
            price = cardbal - buyPrice
            t.append(selectedTicket)
            update_pickle_user(user, price)
            print(selectedTicket)
            buyWindow.showSelectedTicket(selectedTicket)
            print("Card Balance: ", selectedcard.getBalance())
            widget.setCurrentWidget(bookingWindow)
        else:
            buyWindow.Popup()

    buyWindow.ui.BuyTicket.clicked.connect(buy)

    def LoginToApp():
        global NowLoginCustomer
        username = loginPage.ui.username_input.text()
        password = loginPage.ui.password_input.text()
        NowLoginCustomer = LoginWindow().VerifyLogin(username, password)
        if NowLoginCustomer == True:
            return
        else:
            widget.setCurrentWidget(bookingWindow)


    loginPage.ui.loginButton.clicked.connect(LoginToApp)

    def displayHistory():
        user = NowLoginCustomer
        historyWindow.showBookings(user)
        widget.setCurrentWidget(historyWindow)

    bookingWindow.ui.viewBookings.clicked.connect(displayHistory)


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

    app.exec_()



