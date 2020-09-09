from node import Node

class DoublyLinked:
    
    def __init__(self):
        self.head = None
        self.beginer = None

    def add(self, data):
        if self.beginer == None:
            node = Node(data)
            node.sett_next(self.beginer)
            node.sett_bef(self.head)
            self.head = node
            self.beginer = node
        
        else:
            node = Node(data)
            node.sett_next(self.head)
            node.sett_bef(self.head.gett_bef)
            self.head.sett_bef(node)
            self.head = node
  
    def insert(self, data, index):
        pass

    def add_init(self):
        pass 

    def remove(self, index):
        selected_node = self.gett_node(index)
        node_before = selected_node.gett_bef
        node_next = selected_node.gett_next

        node_before.sett_next(selected_node.gett_next)
        node_next.sett_bef(selected_node.gett_bef)
        selected_node.sett_next(None)
        selected_node.sett_bef(None)

    def gett_node(self, index):
        head = self.head
        
        for i in range(index):
            if head:
                head = head.gett_next
            else:
                raise IndexError("index out range")
        
        return head 

    def info_node(self, index):
        selected_node = self.gett_node(index)
        return print(f"{selected_node.gett_bef} <- {selected_node.data} -> {selected_node.gett_next}")

    def __repr__(self):
        head = self.head
        append_list = []
        while head:
            append_list.append(str(head.data))
            head = head.gett_next
        
        append_list.append("none")
        return "->".join(append_list)