# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BookingWindowCKIzED.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 227)
        self.dropdown_departure = QComboBox(Form)
        self.dropdown_departure.addItem("")
        self.dropdown_departure.setObjectName(u"dropdown_departure")
        self.dropdown_departure.setGeometry(QRect(20, 20, 141, 32))
        font = QFont()
        font.setPointSize(15)
        self.dropdown_departure.setFont(font)
        self.dropdown_destination = QComboBox(Form)
        self.dropdown_destination.addItem("")
        self.dropdown_destination.setObjectName(u"dropdown_destination")
        self.dropdown_destination.setGeometry(QRect(170, 20, 141, 32))
        self.dropdown_destination.setFont(font)
        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(480, 20, 110, 22))
        self.dropdow_tickettype = QComboBox(Form)
        self.dropdow_tickettype.addItem("")
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 131, 32))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(470, 130, 131, 32))

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
        self.pushButton.setText(QCoreApplication.translate("Form", u"go back to login", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"go to ticket select", None))
    # retranslateUi

