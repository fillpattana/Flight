from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from HistoryWindow import *

class historyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_HistoryPage()
        self.ui.setupUi(self)