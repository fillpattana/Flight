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
    loginPage.ui.loginButton.clicked.connect(lambda : widget.setCurrentWidget(bookingWindow))

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
        time = bookingWindow.ui.dateEdit.dateTime()
        print(time)

        purchaseWindow.parameter()
        widget.setCurrentWidget(purchaseWindow)


    bookingWindow.ui.GenerateTicks.clicked.connect(abcdee)




    app.exec_()



