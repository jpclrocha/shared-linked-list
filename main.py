from node import Node
from linked_list import LinkedList


l1 = LinkedList()
print("----- BLOCO 1 -----")
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(5)
l1.append(6)
l1.append(7)
l1.append(8)
print(l1)


print("\n----- BLOCO 2 -----")
l1.pop()
l1.pop()
l1.pop()
print(l1)

print("\n----- BLOCO 3 -----")
print(l1.search(10))
print(l1.search(6))