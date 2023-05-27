# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLPBQUP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_HistoryPage(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(483, 374)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.BookingsLabel = QLabel(Form)
        self.BookingsLabel.setObjectName(u"BookingsLabel")
        self.BookingsLabel.setGeometry(QRect(10, 40, 461, 321))
        self.BookingsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.goBack = QPushButton(Form)
        self.goBack.setObjectName(u"pushButton")
        self.goBack.setGeometry(QRect(10, 330, 100, 32))
        self.goNext = QPushButton(Form)
        self.goNext.setObjectName(u"pushButton_2")
        self.goNext.setGeometry(QRect(370, 330, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Your Bookings:", None))
        self.BookingsLabel.setText(QCoreApplication.translate("Form", u"BOOKINGS PRINT HERE", None))
        self.goBack.setText(QCoreApplication.translate("Form", u"goback", None))
        self.goNext.setText(QCoreApplication.translate("Form", u"gonext", None))
    # retranslateUi


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    historyPage = QMainWindow()
    w = Ui_HistoryPage()
    w.setupUi(historyPage)
    historyPage.show()
    sys.exit(app.exec_())