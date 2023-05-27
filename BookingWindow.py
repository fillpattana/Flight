# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BookingWindowCKIzED.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_BookingPage(object):
    destination = ["United States", "United Kingdom", "United Arab Emirates", "Ukraine", "Hong Kong", "Turkey",
                   "Thailand", "Taiwan", "Switzerland", "Spain", "South Africa", "Singapore", "Russia",
                   "Papua New Guinea", "Pakistan", "Norway", "Nigeria", "New Zealand", "Netherlands", "Morocco",
                   "Mexico", "Maldives", "Malaysia", "South Korea", "Jordan", "Japan", "Italy", "Indonesia",
                   "India", "Guinea", "Germany", "France", "Egypt", "Denmark", "Czech Republic", "Cuba",
                   "Colombia", "China", "Canada", "Cambodia", "Myanmar", "Brazil", "Belgium", "Bangladesh",
                   "Austria", "Australia", "Argentina", "Afghanistan"]

    classTicket = ["Business", "FirstClass", "Economy"]

    currentDate = QDateTime.currentDateTime()


    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 227)

        sortedDestination = sorted(self.destination)
        self.dropdown_departure = QComboBox(Form)
        self.dropdown_departure.addItems(sortedDestination)
        self.dropdown_departure.setObjectName(u"dropdown_departure")
        self.dropdown_departure.setGeometry(QRect(20, 20, 141, 32))

        font = QFont()
        font.setPointSize(15)

        self.dropdown_departure.setFont(font)

        self.dropdown_destination = QComboBox(Form)
        self.dropdown_destination.addItems(sortedDestination)
        self.dropdown_destination.setObjectName(u"dropdown_destination")
        self.dropdown_destination.setGeometry(QRect(170, 20, 141, 32))
        self.dropdown_destination.setFont(font)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(480, 20, 110, 22))
        self.dateEdit.setDateTime(self.currentDate)

        self.dropdow_tickettype = QComboBox(Form)
        self.dropdow_tickettype.addItems(self.classTicket)
        self.dropdow_tickettype.setObjectName(u"dropdow_tickettype")
        self.dropdow_tickettype.setGeometry(QRect(320, 20, 141, 32))
        self.dropdow_tickettype.setFont(font)

        self.viewBookings = QPushButton(Form)
        self.viewBookings.setObjectName(u"viewBookings")
        self.viewBookings.setGeometry(QRect(10, 170, 171, 51))

        self.GenerateTicks = QPushButton(Form)
        self.GenerateTicks.setObjectName(u"GenerateTicks")
        self.GenerateTicks.setGeometry(QRect(450, 60, 141, 41))
        font1 = QFont()
        font1.setPointSize(17)
        self.GenerateTicks.setFont(font1)

        self.goToLogin = QPushButton(Form)
        self.goToLogin.setObjectName(u"pushButton")
        self.goToLogin.setGeometry(QRect(10, 130, 131, 32))
        self.goToTicketSelect = QPushButton(Form)
        self.goToTicketSelect.setObjectName(u"pushButton_4")
        self.goToTicketSelect.setGeometry(QRect(470, 130, 131, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dropdown_departure.setItemText(0, QCoreApplication.translate("Form", u"Departure", None))

        self.dropdown_destination.setItemText(0, QCoreApplication.translate("Form", u"Destination", None))

        self.dropdow_tickettype.setItemText(0, QCoreApplication.translate("Form", u"Ticket Type", None))

        self.viewBookings.setText(QCoreApplication.translate("Form", u"View My Bookings", None))
        self.GenerateTicks.setText(QCoreApplication.translate("Form", u"Find Tickets", None))
        self.goToLogin.setText(QCoreApplication.translate("Form", u"go back to login", None))
        self.goToTicketSelect.setText(QCoreApplication.translate("Form", u"go to ticket select", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    bookingPage = QMainWindow()
    w = Ui_BookingPage()
    w.setupUi(bookingPage)
    bookingPage.show()
    sys.exit(app.exec_())

