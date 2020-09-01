class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    @property
    def gett_next(self):
        return self.next

    @property
    def gett_data(self):
        return self.data

    def sett_next(self, new_next):
        self.next = new_next
    
    def sett_data(self, new_data):
        self.data = new_data