# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerChJjhi.ui'
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
        Form.resize(627, 513)
        self.regis_name_input = QLineEdit(Form)
        self.regis_name_input.setObjectName(u"regis_name_input")
        self.regis_name_input.setGeometry(QRect(140, 30, 421, 31))
        font = QFont()
        font.setPointSize(17)
        self.regis_name_input.setFont(font)
        self.label_b = QLabel(Form)
        self.label_b.setObjectName(u"label_b")
        self.label_b.setGeometry(QRect(50, 30, 91, 31))
        self.label_b.setFont(font)
        self.label_c = QLabel(Form)
        self.label_c.setObjectName(u"label_c")
        self.label_c.setGeometry(QRect(50, 70, 91, 31))
        self.label_c.setFont(font)
        self.regis_age_input = QLineEdit(Form)
        self.regis_age_input.setObjectName(u"regis_age_input")
        self.regis_age_input.setGeometry(QRect(140, 70, 421, 31))
        self.regis_age_input.setFont(font)
        self.regis_user_input = QLineEdit(Form)
        self.regis_user_input.setObjectName(u"regis_user_input")
        self.regis_user_input.setGeometry(QRect(140, 110, 421, 31))
        self.regis_user_input.setFont(font)
        self.regis_pw_input = QLineEdit(Form)
        self.regis_pw_input.setObjectName(u"regis_pw_input")
        self.regis_pw_input.setGeometry(QRect(140, 150, 421, 31))
        self.regis_pw_input.setFont(font)
        self.label_d = QLabel(Form)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setGeometry(QRect(50, 110, 91, 31))
        self.label_d.setFont(font)
        self.label_e = QLabel(Form)
        self.label_e.setObjectName(u"label_e")
        self.label_e.setGeometry(QRect(50, 150, 91, 31))
        self.label_e.setFont(font)
        self.label_f = QLabel(Form)
        self.label_f.setObjectName(u"label_f")
        self.label_f.setGeometry(QRect(270, 190, 91, 31))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.label_f.setFont(font1)
        self.label_g = QLabel(Form)
        self.label_g.setObjectName(u"label_g")
        self.label_g.setGeometry(QRect(50, 210, 91, 31))
        self.label_g.setFont(font)
        self.label_i = QLabel(Form)
        self.label_i.setObjectName(u"label_i")
        self.label_i.setGeometry(QRect(50, 300, 91, 31))
        self.label_i.setFont(font)
        self.label_h = QLabel(Form)
        self.label_h.setObjectName(u"label_h")
        self.label_h.setGeometry(QRect(90, 240, 91, 31))
        self.label_h.setFont(font)
        self.label_j = QLabel(Form)
        self.label_j.setObjectName(u"label_j")
        self.label_j.setGeometry(QRect(90, 330, 91, 31))
        self.label_j.setFont(font)
        self.credit_pin = QLineEdit(Form)
        self.credit_pin.setObjectName(u"credit_pin")
        self.credit_pin.setGeometry(QRect(160, 240, 421, 31))
        self.credit_pin.setFont(font)
        self.debit_pin = QLineEdit(Form)
        self.debit_pin.setObjectName(u"debit_pin")
        self.debit_pin.setGeometry(QRect(160, 330, 421, 31))
        self.debit_pin.setFont(font)
        self.addDebitCard = QPushButton(Form)
        self.addDebitCard.setObjectName(u"addDebitCard")
        self.addDebitCard.setGeometry(QRect(480, 360, 101, 51))
        self.addCreditCard = QPushButton(Form)
        self.addCreditCard.setObjectName(u"addCreditCard")
        self.addCreditCard.setGeometry(QRect(480, 270, 101, 51))
        self.goToLogin = QPushButton(Form)
        self.goToLogin.setObjectName(u"goToLogin")
        self.goToLogin.setGeometry(QRect(200, 440, 251, 32))
        self.gobacktologin = QPushButton(Form)
        self.gobacktologin.setObjectName(u"gobacktologin")
        self.gobacktologin.setGeometry(QRect(10, 480, 131, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.regis_name_input.setText("")
        self.label_b.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_c.setText(QCoreApplication.translate("Form", u"Age:", None))
        self.regis_age_input.setText("")
        self.regis_user_input.setText("")
        self.regis_pw_input.setText("")
        self.label_d.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.label_e.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.label_f.setText(QCoreApplication.translate("Form", u"Add Cards", None))
        self.label_g.setText(QCoreApplication.translate("Form", u"Credit Card:", None))
        self.label_i.setText(QCoreApplication.translate("Form", u"Debit Card:", None))
        self.label_h.setText(QCoreApplication.translate("Form", u"Enter Pin:", None))
        self.label_j.setText(QCoreApplication.translate("Form", u"Enter Pin:", None))
        self.credit_pin.setText("")
        self.debit_pin.setText("")
        self.addDebitCard.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.addCreditCard.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.goToLogin.setText(QCoreApplication.translate("Form", u"Sign in", None))
        self.gobacktologin.setText(QCoreApplication.translate("Form", u"go back to login", None))
    # retranslateUi

