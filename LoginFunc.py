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
        card.setPin(pin)
    elif card_type == "debitCard":
        card = DebitCard(name, pin)
        card.setPin(pin)
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

import pickle

def update_pickle_user(user, price):
    username = user.name
    try:
        with open('user_data.pkl', 'rb') as file:
            users = pickle.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    if username not in users:
        print("User does not exist.")
        return

    # Update the limit or balance for the selected card in the user's cards list
    for card in user.cards:
        if card == user.cards:
            if isinstance(card, CreditCard):
                card.setLimit(price)
            elif isinstance(card, DebitCard):
                card.setBalance(price)
            break

    # Save the modified user object back into the pickle file
    with open('user_data.pkl', 'wb') as file:
        pickle.dump(users, file)

    print("Card limit/balance updated successfully.")

# Assuming you have the user and selectedcard objects available
# update_pickle_user(user, 5000)


