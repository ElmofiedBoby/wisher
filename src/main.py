from user import User
from item import Item
from storage import *

def is_logged_in(current_user, logged_in):
    if current_user is None or logged_in is False:
        return False
    else:
        return True

def process_inputs(user_input, logged_in, current_user):
    if user_input == "quit":
        print("Quitting...")

    elif user_input == "create":
        username = input("Username: ")
        password = input("Password: ")
        add_user(User(username, password, "Nithin", "Joseph"))
        print("Account created successfully!")

    elif user_input == "login":
        user_found = False
        potential = None
        username = input("Username: ")

        for user in get_users():
            if user.get_uname() == username:
                user_found = True
                current_user = user
                break

        if user_found is True:
            password = input("Password: ")
            if password == current_user.get_password():
                logged_in = True
                print("Logged in!")
            else:
                current_user = None
                print("Incorrect Password!")
        else:
            current_user = None
            print("User not found!")

    elif user_input == "logout":
        if is_logged_in(current_user, logged_in) is False:
            print("You aren't logged in.")
        else:
            current_user = None
            logged_in = False
            print("Logged out!")
    
    elif user_input == "add":
        if is_logged_in(current_user, logged_in) is False:
            print("You aren't logged in.")
        else:
            item = input("Item name: ")
            cost = input("Item cost: $")
            link = input("Link to item: ")
            wish = Item(item, current_user, None, False, None, link, cost)
            current_user.add_wish(wish)
            print("{} added to wishlist!".format(wish.get_name()))

    elif user_input == "list":
        if is_logged_in(current_user, logged_in) is False:
            print("You aren't logged in.")

        else:
            current_user.list_wishes()
    
    else:
        print("Invalid Command!")
    
    return logged_in, current_user

def main():
    print("Welcome to Wisher!")

    logged_in = False
    current_user = None

    user_input = input("> ")
    if user_input != "quit":
        logged_in, current_user = process_inputs(user_input, logged_in, current_user)
    else:
        print("Quitting...")

    while user_input != "quit":
        user_input = input("> ")
        logged_in, current_user = process_inputs(user_input,  logged_in, current_user)

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main() 