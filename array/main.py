from lista import LinkedList
from node import Node

lista = LinkedList()
lista.add_init(1)
lista.add_init(2)
lista.add_init(3)
lista.add_init(4)
lista.add_init(5)
lista.add_init(6)
print(lista)
lista.insert(55555, 3)
print(lista)
lista.remove(3)
print(lista)
lista.insert(2, 2)
print(lista)
# lista.remove(4)
