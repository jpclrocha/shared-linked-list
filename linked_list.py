from node import Node
class LinkedList:
    def __init__(self):
        self.head = None #O inicio da lista
        self.tail = None #O fim da lista
        
    def is_empty(self):
        return self.head == None
    
    def append(self, valor):
        node = Node(valor)
        if(self.head == None):
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            temp.set_next(node)
            self.tail = node
            
    def pop(self):
        if(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            temp = self.head.get_next()
            self.head = temp
        
        
    def __str__(self):
        curr = self.head
        text = ""
        while curr != None:
            text += str(curr.get_data())
            if(curr.get_next() != None):
                text += " => "
            curr = curr.get_next()
        return text