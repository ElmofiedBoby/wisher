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
        filehandler = open('save_data', 'wb')
        pickle.dump(self.users, filehandler)

    def load(self):
         filehandler = open('save_data', 'rb')
         self.users = pickle.load(filehandler)

         return self.users