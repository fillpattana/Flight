from RegisterWindow import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from LoginFunc import *

import pickle
from creditCard import*
from debitCard import*
from customer import *


class registerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RegisterPage()
        self.ui.setupUi(self)

    def addNewUser(self, name1, age, username1, password1):
        register_user(name1, age, username1, password1)

    def infos(self):
        print_user_data()

    def addCredit(self, username2, card_type, name2, pin):
        create_card(username2, card_type, name2, pin)

    def addDebit(self, username3, card_type, name3, pin):
        create_card(username3, card_type, name3, pin)






