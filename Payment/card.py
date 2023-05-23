class Card():
    
    def __init__(self, fname, lname, balance, id, pin):
        self.fname = fname
        self.lname = lname
        self.balance = balance
        self.pin = pin
        self.id = 1234
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)












if __name__ == '__main__':
    obj1 = Card("ja", "jo", 1, 000, 2)
    print(obj1.fname)