# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLPBQUP.ui'
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 330, 100, 32))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(370, 330, 100, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Your Bookings:", None))
        self.BookingsLabel.setText(QCoreApplication.translate("Form", u"BOOKINGS PRINT HERE", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"goback", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"gonext", None))
    # retranslateUi

