from node import Node


class LinkedListVaziaException(Exception):
    pass


class LinkedList:
    def __init__(self):
        self.head = None  # O inicio da lista
        self.tail = None  # O fim da lista

    def is_empty(self):
        return not self.head
    
    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count

    def append(self, valor):
        node = Node(valor)
        if (self.head is None):
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            temp.set_next(node)
            self.tail = node

    def pop(self):
        try:
            if self.head is None:
                raise LinkedListVaziaException("Lista vazia! Elementos não podem ser removidos!")

            value_removed = self.head.get_data()
            if self.head.get_next() is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()

            return value_removed
        except LinkedListVaziaException as e:
            print(e)
            
    
    def search(self, item):
        try:
            if(self.is_empty()):
                raise LinkedListVaziaException("Lista vazia!")
        
            curr = self.head
            while curr is not None:
                if(curr.get_data() == item):
                    return True
                curr = curr.get_next()
                
            return False
        except LinkedListVaziaException as e:
            print(e)

    def __str__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.get_data()))
            curr = curr.get_next()
        return " => ".join(elements)
