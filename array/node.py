class Node:
    def __init__(self, data):
        self.data = data
        self.next = 0
    
    @property
    def getter_data(self):
        return self.data
    
    def setter_data(self, new_data):
        self.data = new_data
    
    @property
    def getter_next(self):
        return self.next
    
    def setter_next(self, new_next):
        self.next = new_next