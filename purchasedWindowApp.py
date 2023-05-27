from PurchaseWindow import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ticketGenerator import *
import datetime


class purchasedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PurchasePage()
        self.ui.setupUi(self)

    def parameter(self, destination, departure, ticketType, date):
        passengerName = "Kittiphong Thachaphat"  # TODO Get name from customer object
        day = date.day()
        year = date.year()
        month = date.month()
        date = datetime.date(year, month, day)
        tickets = generateTicket(passengerName, destination, departure, date, ticketType)
        w_msg = QErrorMessage()

        if len(tickets) == 0:
            w_msg.showMessage("Ticket Doesn't Exist!!")
            w_msg.exec_()

        else:
            while len(tickets) != 5:
                tickets.append("Ticket " + str(len(tickets) + 1) + "\nNOT AVAILABLE!!")
            self.ui.ticket1.setText(tickets[0].__str__())
            self.ui.ticket2.setText(tickets[1].__str__())
            self.ui.ticket3.setText(tickets[2].__str__())
            self.ui.ticket4.setText(tickets[3].__str__())
            self.ui.ticket5.setText(tickets[4].__str__())

        return tickets

    def confirm(self, ticket):
        qm = QMessageBox()
        text = "Are you sure this is the ticket you want to purchase?\n\n" + ticket.__str__()
        qm.setWindowTitle("Ticket Confirmation")
        qm.setText(text)
        qm.setStandardButtons(QMessageBox.StandardButton.Yes |
                              QMessageBox.StandardButton.No)
        x = qm.exec_()

        if x == QMessageBox.StandardButton.Yes.value:
            return ticket

        else:
            return




