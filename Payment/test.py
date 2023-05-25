import ZODB, ZODB.FileStorage
import transaction

from card import Card
from creditCard import CreditCard
from debitCard import DebitCard


# Connect to the ZODB database
storage = ZODB.FileStorage.FileStorage('/Users/akararatpattanamontri/Documents/FlightSEP/Flight/Payment.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

# Create an instance of CreditCard
card1 = CreditCard("Jackson Blue", "1111")
card1.setNumber()

card2 = DebitCard("Malisa Brown", "2222")
card2.setNumber()

# Create a dictionary attribute in the root CreditCard to store the card and print status
def create_dict_credit(card):
    if not hasattr(root, 'cards'):
        root.cards = {}
    root.cards['card1'] = card
    transaction.commit()
    for key in root.cards.keys():
        item = root.cards[key]
        print("Name:", item.getName())
        print("Pin:", item.getPin())
        print("Credit:", item.getCredit())
        print("Limit:", item.getLimit())
        print("Number:", item.getNumber())
        print()
        
# Create a dictionary attribute in the root DebitCard to store the card and print status
def create_dict_debit(card):
    if not hasattr(root, 'cards'):
        root.cards = {}
    root.cards['card1'] = card
    transaction.commit()
    for key in root.cards.keys():
        item = root.cards[key]
        print("Name:", item.getName())
        print("Pin:", item.getPin())
        print("Balance:", item.getBalance())
        print("Number:", item.getNumber())
        print()


create_dict_credit(card1)       
create_dict_debit(card2) 


# Close the connection
connection.close()