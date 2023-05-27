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
        return

    if username in users:
        user = users[username]
        if user.pw == password:
            print("Login successful.")
            return
    print("Invalid username or password.")


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


# Example usage
register_user("user1", "password123", "John Doe", 25)
create_card("user1", "creditCard", "John Doe", 1234)
create_card("user1", "debitCard", "John Doe", 4321)
login("user1", "password123")
print_user_data()
