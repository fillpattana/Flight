from LoginWindow import *
from LoginFunc import *


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginPage()
        self.ui.setupUi(self)

    def VerifyLogin(self, un, pw):
        check = login(un, pw)
        popup = QErrorMessage()
        if not check:
            popup.showMessage("invalid username or password")
            popup.exec_()
            return True
        else:
            return check




