from RegisterWindow import *

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class registerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterPage()
        self.ui.setupUi(self)

