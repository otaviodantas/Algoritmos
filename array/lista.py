from node import Node


class LinkedList():

    def __init__(self):
        self.head = None

    def add_init(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data, index_node: int):
        node = Node(data)
        before_node = self._get_node(index_node - 1)
        node.sett_next(before_node.gett_next)
        before_node.sett_next(node)

    def remove(self, index_node):
        before_node = self._get_node(index_node - 1)
        want_remove_node = self._get_node(index_node)
        before_node.sett_next(want_remove_node.gett_next)

    def _get_node(self, index_node: int):
        select_node = self.head
        for i in range(index_node):
            if select_node:
                select_node = select_node.gett_next
            else:
                raise IndexError("list index out of range")
        return select_node

    def __repr__(self):
        arrow_count = self.head
        data_list = []
        while arrow_count:
            data_list.append(str(arrow_count.gett_data))
            arrow_count = arrow_count.gett_next

        data_list.append("None")
        return " -> ".join(data_list)
