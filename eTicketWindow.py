# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eTicketWindowBCwFre.ui'
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
        Form.resize(355, 303)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 231, 21))
        self.PurchasedTicketLabel = QLabel(Form)
        self.PurchasedTicketLabel.setObjectName(u"PurchasedTicketLabel")
        self.PurchasedTicketLabel.setGeometry(QRect(10, 40, 331, 191))
        self.PurchasedTicketLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.goback = QPushButton(Form)
        self.goback.setObjectName(u"goback")
        self.goback.setGeometry(QRect(10, 260, 100, 32))
        self.gonext = QPushButton(Form)
        self.gonext.setObjectName(u"gonext")
        self.gonext.setGeometry(QRect(240, 260, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"THANK YOU FOR YOUR PURCHASE!", None))
        self.PurchasedTicketLabel.setText(QCoreApplication.translate("Form", u"PURCHASED TICKET", None))
        self.goback.setText(QCoreApplication.translate("Form", u"goback", None))
        self.gonext.setText(QCoreApplication.translate("Form", u"gonext", None))
    # retranslateUi
