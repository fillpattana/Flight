# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerwfsJoG.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Ui_BuyWindow(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 91, 16))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)


        self.selectCard = QComboBox(Form)
        cardsChoose = ["Select A Card", "1", "2", "3", "4", "5"]
        self.selectCard.addItems(cardsChoose)
        self.selectCard.setObjectName(u"selectCard")
        self.selectCard.setGeometry(QRect(130, 20, 181, 32))

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 91, 16))
        self.label_2.setFont(font)
        self.enterPin = QLineEdit(Form)
        self.enterPin.setObjectName(u"enterPin")
        self.enterPin.setGeometry(QRect(30, 130, 331, 51))
        self.enterPin.setEchoMode(QLineEdit.EchoMode.Password)
        font1 = QFont()
        font1.setPointSize(20)
        self.enterPin.setFont(font1)

        self.BuyTicket = QPushButton(Form)
        self.BuyTicket.setObjectName(u"BuyTicket")
        self.BuyTicket.setGeometry(QRect(30, 210, 141, 51))

        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        self.BuyTicket.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select Card:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Enter Pin:", None))
        self.enterPin.setText("")
        self.BuyTicket.setText(QCoreApplication.translate("Form", u"CONFIRM", None))
    # retranslateUi


# from ctest import *

# class BuyTicketWindow(QWidget):
#     def __init__(self):
#         QWidget.__init__(self, None)
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    buyWindowPage = QMainWindow()
    w = Ui_BuyWindow
    w.setupUi(buyWindowPage)
    buyWindowPage.show()
    sys.exit(app.exec_())

