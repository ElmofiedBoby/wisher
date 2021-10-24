class Item:

    def __init__(self, name, owner, claimee, claimed_status, type, link, cost):
        self.__name = name
        self.__owner = owner
        self.__claimee = claimee
        self.__claim_status = claimed_status
        self.__type = type
        self.__link = link
        self.__cost = cost
        self.__place = -1
        
    def get_name(self):
        return self.__name

    def get_owner(self):
        return self.__owner

    def get_claimee(self):
        return self.__claimee

    def get_claim_status(self):
        return self.__claim_status

    def get_type(self):
        return self.__type

    def get_link(self):
        return self.__link

    def get_cost(self):
        return self.__cost

    def get_place(self):
        return self.__place


    def set_name(self, name):
        self.__name = name

    def set_claimee(self, claimee):
        self.__claimee = claimee

    def set_claim_status(self, status):
        self.__claim_status = status

    def set_type(self, type):
        self.__type = type

    def set_link(self, link):
        self.__link = link

    def set_cost(self, cost):
        self.__cost = cost

    def set_place(self, place):
        self.__place = place