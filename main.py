from node import Node
from linked_list import LinkedList

v1 = Node(1)
v2 = Node(2)
v3 = Node(3)
v4 = Node(4)
v5 = Node(5)
v6 = Node(6)
v7 = Node(7)
v8 = Node(8)


l1 = LinkedList()
print("----- BLOCO 1 -----")
l1.append(v1)
l1.append(v2)
l1.append(v3)
l1.append(v4)
l1.append(v5)
l1.append(v6)
l1.append(v7)
l1.append(v8)
print(l1)


print("\n----- BLOCO 2 -----")
l1.pop()
l1.pop()
l1.pop()
print(l1)