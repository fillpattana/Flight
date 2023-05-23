from card import Card

class creditCard(Card):
    
    def __init__(self, fname, lname, id, pin):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.pin = pin
        self.limit = None
    
    def confirmPay():
        pass
    
    def setLimit(self, limit):
        self.limit = limit
    
















if __name__ == '__main__':
    obj2 = creditCard("ji", "ju", 9902, 3)
    print(obj2.fname, obj2.lname, obj2.pin)
