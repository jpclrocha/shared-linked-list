from node import Node
import threading

'''
    A implementação é a mesma do outro arquivo, porém com lock para resolver os problemas de concorrencia
'''

class LinkedListVaziaException(Exception):
    pass


class LinkedListLock:
    def __init__(self):
        self.head: Node | None = None  # O inicio da lista
        self.tail: Node | None = None  # O fim da lista
        self.list_lock = threading.Lock()

    def is_empty(self) -> bool:
        with self.list_lock:
            return not self.head

    def size(self) -> int:
        with self.list_lock:
            count = 0
            curr = self.head
            while curr is not None:
                count += 1
                curr = curr.get_next()
            return count

    def append(self, valor: any) -> None:
        with self.list_lock:
            node = Node(valor)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.set_next(node)
                self.tail = node

    def pop(self) -> any:
        if self.is_empty():
            raise LinkedListVaziaException("Lista vazia! Elementos não podem ser removidos!")
        
        with self.list_lock:
            value_removed = self.head.get_data()
            if self.head.get_next() is None:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next()
            
            return value_removed

    def search(self, item: any) -> bool:
        if self.is_empty():
            raise LinkedListVaziaException("Lista vazia!")
        
        with self.list_lock:
            curr = self.head
            while curr is not None:
                if curr.get_data() == item:
                    return True
                curr = curr.get_next()

            return False

    def __str__(self) -> str:
        with self.list_lock:
            elements = []
            curr = self.head
            while curr:
                elements.append(str(curr.get_data()))
                curr = curr.get_next()
            return " => ".join(elements)
