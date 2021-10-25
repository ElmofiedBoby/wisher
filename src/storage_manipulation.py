from user import *
from store import store_data
import numpy as np
import pickle

class store:

    users = []

    def add_user(self, user):
        store.users.append(user)

    def get_users(self):
        return store.users

    def get_user(self, user_string):
        for user in store.users:
            if user_string == user.get_uname():
                return user

        return None

    def view_list(self, user):
        user.list_wishes()

    def save(self):
        for user in store.users:
            store_data.get_users().append(user)

        filehandler = open('save_data', 'wb')
        save_data = store_data()
        pickle.dump(save_data, filehandler)

    def load(self):
         filehandler = open('save_data', 'rb')
         save_data = pickle.load(filehandler)
         store.users = []
         for user in save_data.get_users():
             store.users.append(user)