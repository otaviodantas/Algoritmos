
from node import Node


class LinList:

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        while current != None:
            content = current.getter_data
            current = current.getter_next
            print(content)

    def add(self, data):
        node = Node(data)
        node.setter_next(self.head)
        self.head = node

    def size_list(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getter_next

        return count

    def search(self, data):
        current = self.head
        found = False

        while(current != None and not found):
            if current.getter_data == data:
                found = True
            else:
                current = current.getter_next

        return found

    def remove(self, item):
        found = False
        previus = None
        current = self.head
        while not found:
            if current.getter_data == item:
                found = True
            else:
                previus = current
                current = current.getter_next

        if previus == None:
            self.head = current.getter_next
        else:
            previus.setter_next(current.getter_next)
