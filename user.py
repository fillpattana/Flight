class CreateUser():
    
    def __init__(self, name, age, usern, pw):
        self.name = name
        self.age = age
        self.usern = usern
        self.pw = pw
        self.ticketBought = []

    def getTicket(self):
        return self.ticketBought

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getUser(self):
        return self.usern
    
    def getPass(self):
        return self.pw
    
    def setUser(self, username):
        self.usern = username
        
    def setPass(self, password):
        self.pw = password
    
    def __str__(self):
        info = "Name: \t\t" + self.name + "\n"
        info += "Age: \t\t" + str(self.age) + "\n"
        info += "User Name: \t" + self.usern + "\n"
        info += "Password: \t" + str(self.pw) + "\n"
        return info

    
if __name__ == '__main__':
    user1 = CreateUser("Jackson Blue", 25, "k", "kk")
    print(user1)
        
        
    