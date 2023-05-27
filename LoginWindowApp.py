from LoginWindow import *


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)

