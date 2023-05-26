# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PurchaseWindowCcUTHh.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(742, 680)
        self.ticket2 = QLabel(Form)
        self.ticket2.setObjectName(u"ticket2")
        self.ticket2.setGeometry(QRect(390, 10, 331, 191))
        font = QFont()
        font.setPointSize(14)
        self.ticket2.setFont(font)
        self.ticket2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ticket3 = QLabel(Form)
        self.ticket3.setObjectName(u"ticket3")
        self.ticket3.setGeometry(QRect(20, 220, 331, 201))
        self.ticket3.setFont(font)
        self.ticket3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ticket1 = QLabel(Form)
        self.ticket1.setObjectName(u"ticket1")
        self.ticket1.setGeometry(QRect(20, 10, 331, 191))
        self.ticket1.setFont(font)
        self.ticket1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ticket4 = QLabel(Form)
        self.ticket4.setObjectName(u"ticket4")
        self.ticket4.setGeometry(QRect(390, 220, 331, 191))
        self.ticket4.setFont(font)
        self.ticket4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.ticket5 = QLabel(Form)
        self.ticket5.setObjectName(u"ticket5")
        self.ticket5.setGeometry(QRect(20, 430, 331, 191))
        self.ticket5.setFont(font)
        self.ticket5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.payTick1 = QPushButton(Form)
        self.payTick1.setObjectName(u"payTick1")
        self.payTick1.setGeometry(QRect(250, 180, 100, 32))
        self.payTick2 = QPushButton(Form)
        self.payTick2.setObjectName(u"payTick2")
        self.payTick2.setGeometry(QRect(620, 180, 100, 32))
        self.payTick4 = QPushButton(Form)
        self.payTick4.setObjectName(u"payTick4")
        self.payTick4.setGeometry(QRect(620, 390, 100, 32))
        self.payTick3 = QPushButton(Form)
        self.payTick3.setObjectName(u"payTick3")
        self.payTick3.setGeometry(QRect(250, 400, 100, 32))
        self.payTick5 = QPushButton(Form)
        self.payTick5.setObjectName(u"payTick5")
        self.payTick5.setGeometry(QRect(250, 600, 100, 32))
        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 640, 100, 32))
        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(630, 640, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.ticket2.setText(QCoreApplication.translate("Form", u"Ticket2", None))
        self.ticket3.setText(QCoreApplication.translate("Form", u"Ticket3", None))
        self.ticket1.setText(QCoreApplication.translate("Form", u"Ticket1", None))
        self.ticket4.setText(QCoreApplication.translate("Form", u"Ticket4", None))
        self.ticket5.setText(QCoreApplication.translate("Form", u"Ticket5", None))
        self.payTick1.setText(QCoreApplication.translate("Form", u"PURCHASE", None))
        self.payTick2.setText(QCoreApplication.translate("Form", u"PURCHASE", None))
        self.payTick4.setText(QCoreApplication.translate("Form", u"PURCHASE", None))
        self.payTick3.setText(QCoreApplication.translate("Form", u"PURCHASE", None))
        self.payTick5.setText(QCoreApplication.translate("Form", u"PURCHASE", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"goback", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"gonext", None))
    # retranslateUi

