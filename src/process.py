from user import User
from item import Item
from storage import *

from getpass import getpass

def is_logged_in(current_user, logged_in):
    if current_user is None or logged_in is False:
        return False
    else:
        return True

def process_inputs(user_input, logged_in, current_user):

    inputs = user_input.split(" ")

    if user_input == "quit":
        print("Quitting...")

    elif user_input == "create":
        username = input("Username: ")
        password = input("Password: ")
        add_user(User(username, password, "Nithin", "Joseph"))
        print("Account created successfully!")

    elif inputs[0] == "login" and len(inputs) == 2:
        user_found = False
        username = inputs[1]

        for user in get_users():
            if user.get_uname() == username:
                user_found = True
                current_user = user
                break

        if user_found is True:
            password = getpass()
            if password == current_user.get_password():
                logged_in = True
                print("Logged in! Welcome {} :D".format(current_user.get_fname()))
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

    elif inputs[0] == "list":
        if is_logged_in(current_user, logged_in) is False:
            print("You aren't logged in.")

        else:
            if(len(inputs) == 1):
                current_user.list_wishes()
            elif(len(inputs) == 2):
                user = inputs[1]
                user_f = get_user(user)
                if(user_f != None):
                    view_list(user_f)
                else:
                    print("User not found")
            else:
                print("Invalid Arguments!")
    
    else:
        print("Invalid Command!")
    
    return logged_in, current_user