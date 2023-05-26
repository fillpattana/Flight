# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerXjbDJV.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(523, 421)
        self.username_input = QLineEdit(Form)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(110, 40, 371, 41))
        font = QFont()
        font.setPointSize(17)
        self.username_input.setFont(font)
        self.label_username = QLabel(Form)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(30, 40, 81, 41))
        self.label_username.setFont(font)
        self.label_password = QLabel(Form)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setGeometry(QRect(30, 90, 81, 41))
        self.label_password.setFont(font)
        self.password_input = QLineEdit(Form)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(110, 90, 371, 41))
        self.password_input.setFont(font)
        self.loginButton = QPushButton(Form)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(160, 150, 211, 71))
        font1 = QFont()
        font1.setPointSize(24)
        self.loginButton.setFont(font1)
        self.registerButton = QPushButton(Form)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(90, 290, 351, 41))
        self.label_a = QLabel(Form)
        self.label_a.setObjectName(u"label_a")
        self.label_a.setGeometry(QRect(90, 270, 351, 20))
        self.goToBooking = QPushButton(Form)
        self.goToBooking.setObjectName(u"goToBooking")
        self.goToBooking.setGeometry(QRect(400, 380, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_username.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_a.setText(QCoreApplication.translate("Form", u"dont have an account?", None))
        self.goToBooking.setText(QCoreApplication.translate("Form", u"go to Booking", None))
    # retranslateUi

