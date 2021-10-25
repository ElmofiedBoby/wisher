from user import *
from item import Item
import numpy as np

users = []
save_data = np.asarray(users)

users.append(User("nithliveslife", "1234", "Nithin", "Joseph"))
users.append(User("testuser", "5678", "Lorem", "Ipsum"))
users[1].add_wish(Item("Laptop", users[1], None, False, None, "amazon.com", "1400"))

def add_user(user):
    users.append(user)

def get_users():
    return users

def get_user(user_string):
    for user in users:
        if user_string == user.get_uname():
            return user

    return None

def view_list(user):
    user.list_wishes()

def update():
    save_data = np.asarray(users)

def save():
    np.savetxt('save_data.csv', save_data, delimiter=',')

def load():
    save_data = np.loadtxt('save_data.csv', delimiter=',')