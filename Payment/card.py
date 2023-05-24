class Card():
    
    def __init__(self, name, balance, pin, bank):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.bank = bank
        self.id = 1234
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)













if __name__ == '__main__':
    obj1 = Card("ja", "jo", 1, 000, 2)
    print(obj1.fname)