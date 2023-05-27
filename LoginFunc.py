import pickle
from creditCard import*
from debitCard import*
from customer import *


def register_user(username, password, name, age):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        users = {}

    if username in users:
        print("Username already exists.")
        return

    new_customer = Customer(name, age, username, password)
    users[username] = new_customer

    with open('user_data.pkl', 'wb') as file:
        pickle.dump(users, file)

    print("Registration successful.")
    return new_customer

def create_card(username, card_type, name, pin):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    if username not in users:
        print("User does not exist.")
        return

    user = users[username]
    if card_type == "creditCard":
        card = CreditCard(name, pin)
    elif card_type == "debitCard":
        card = DebitCard(name, pin)
    else:
        print("Invalid card type.")
        return

    if not hasattr(user, 'cards'):
        user.cards = []
    user.cards.append(card)

    with open('user_data.pkl', 'wb') as file:
        pickle.dump(users, file)

    print("Card created successfully.")


def login(username, password):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")

    if username in users:
        user = users[username]
        if user.pw == password:
            print("Login successful.\n")
            return user
    print("invalid input")
    return False



def get_user_attribute(user, attribute_name):
    if isinstance(user, Customer):
        if hasattr(user, attribute_name):
            attribute_value = getattr(user, attribute_name)
            if isinstance(attribute_value, list):
                print(f"\n{attribute_name}:\n")
                for value in attribute_value:
                    print(value)
                    print()
            else:
                print(f"{attribute_name}: {attribute_value}")
            return attribute_value
        else:
            print(f"Attribute '{attribute_name}' does not exist for the user.")
    else:
        print("Invalid user object.")
    return None

# def Buy():
#     if get_user_attribute(user, )

def print_user_data():
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    for username, user in users.items():
        print("Username:", username)
        print("Name:", user.name)
        print("Age:", user.age, "\n")
        if hasattr(user, 'cards'):
            print("Customer's Cards\n")
            for card in user.cards:
                print(card)
                print()


def purchase_ticket(ticket):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    username = ticket.get_username()
    if username not in users:
        print("User does not exist.")
        return

    user = users[username]

    # Check if the user has any cards
    if not hasattr(user, 'cards') or len(user.cards) == 0:
        print("No cards available for the user.")
        return

    # Iterate through the user's cards
    for card in user.cards:
        if isinstance(card, CreditCard):
            # Check if the credit limit is sufficient
            if card.getLimit() >= ticket.get_price():
                print("Credit card used for the purchase.")
                user.addTicket(ticket)
                with open('user_data.pkl', 'wb') as file:
                    pickle.dump(users, file)
                return
        elif isinstance(card, DebitCard):
            # Check if the balance is sufficient
            if card.getBalance() >= ticket.get_price():
                print("Debit card used for the purchase.")
                user.addTicket(ticket)
                with open('user_data.pkl', 'wb') as file:
                    pickle.dump(users, file)
                return

    print("Insufficient funds in any card for the purchase.")


# def get_user_cards(username):
#     try:
#         with open('user_data.pkl', 'rb') as file:
#             users = pickle.load(file)
#     except FileNotFoundError:
#         print("No registered users.")
#         return []
#
#     if username not in users:
#         print("User does not exist.")
#         return []
#
#     user = users[username]
#     if not hasattr(user, 'cards'):
#         print("User has no cards.")
#         return []
#
#     cards = user.cards
#     print("User's Cards:")
#     for card in cards:
#         print(card)
#
#     return cards

def get_user_cards(username):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return []

    if username in users:
        user = users[username]
        if isinstance(user, Customer):
            if hasattr(user, 'cards'):
                card_numbers = []
                for card in user.cards:
                    if hasattr(card, 'getNumber'):
                        card_number = card.getNumber()
                        card_numbers.append(card_number)
                return card_numbers
            else:
                print("User has no cards.")
        else:
            print("Invalid user object.")
    else:
        print("User does not exist.")
    return []


def get_user(username):
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return None

    if username in users:
        user = users[username]
        return user

    print("User does not exist.")
    return None


# usern = "JoDo123"
# pw = "JohnnyBalls"
# name = "Joe Doe"
# age = 17


# register_user(usern, pw, name, age)
# create_card(usern, "creditCard", name, 4444)
# create_card(usern, "debitCard", name, 5555)

# print(get_user(usern))
# user = get_user(usern)
# print(user.cards[0].getLimit())


def buyTicket(ticket, cust, i, pin):
    if isinstance(cust.cards[i], CreditCard) and cust.cards[i].getLimit() > ticket.getPrice():
        price = cust.cards[i].getLimit() - ticket.getPrice()
        cust.cards[i].setLimit(price)
        cust.addTicket(ticket)
        for ticks in cust.getTicket():
            print("Ticket Bought")
            print(ticks)
        print("Card Limit: ", cust.cards[i].getLimit())
    elif isinstance(cust.cards[i], DebitCard) and cust.cards[i].getBalance() > ticket.getPrice():
        price = cust.cards[i].getBalance() - ticket.getPrice()
        cust.addTicket(ticket)
        cust.cards[i].setBalance(price)
        for ticks in cust.getTicket():
            print("Ticket Bought")
            print(ticks)
        print("Card Balance: ", cust.cards[i].getBalance())
    else:
        return "poor shit"

    print("\n\n\n", cust.cards[i].getPin)

