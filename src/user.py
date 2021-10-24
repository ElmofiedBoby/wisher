import uuid as id

class User:
    def __init__(self, uname, password, fname, lname):
        self.__uuid = id.uuid4()
        self.__uname = uname
        self.__password = password
        self.__fname = fname
        self.__lname = lname
        self.__name = fname + " " + lname
        self.__wishlist = []
        self.__claims = []
        print("Initialized User {} ({})".format(self.__uname, self.__uuid))

    def get_uuid(self):
        return self.__uuid
        
    def get_uname(self):
        return self.__uname

    def get_password(self):
        return self.__password

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_name(self):
        return self.__name
        
    def set_uname(self, uname):
        self.__uname = uname

    def set_password(self, password):
        self.__password = password

    def set_fname(self, fname):
        self.__fname = fname

    def set_lname(self, lname):
        self.__lname = lname
        
    def add_wish(self, wish):
        size = len(self.__wishlist)+1
        wish.set_place(size)
        self.__wishlist.append(wish)

    def remove_wish(self, wish):
        self.__wishlist.remove(wish)

    def list_wishes(self):
        print("# | $ | Name | Link")
        for wish in self.__wishlist:
            print("{} | ${} | {} | {}".format(wish.get_place(), wish.get_cost(), wish.get_name(), wish.get_link()))