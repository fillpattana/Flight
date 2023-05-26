import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from BuyTicketWindow import Ui_Form


class BuyTicketWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BuyTicketWindow()
    w.show()
    sys.exit(app.exec_())
