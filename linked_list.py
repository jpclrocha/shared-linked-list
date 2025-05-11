from node import Node
import custom_logger
import time

class LinkedListVaziaException(Exception):
    pass


class LinkedList:
    def __init__(self):
        self.head: Node | None = None  # O inicio da lista
        self.tail: Node | None = None  # O fim da lista
        self._logger = custom_logger.Logger()

    def is_empty(self) -> bool:
        return not self.head

    def size(self) -> int:
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count

    def append(self, valor: any) -> None:
        node = Node(valor)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node
            
        self._logger.debug(f"Adicionando {valor} na lista; Estado atual da lista: {self.__str__()}")
        time.sleep(0.1)

    def pop(self) -> any:
        if self.is_empty():
            self._logger.debug("Lista Vazia! Elementos não podem ser removidos!")
            time.sleep(0.1)
            return
            # raise LinkedListVaziaException("Lista vazia! Elementos não podem ser removidos!")

        value_removed = self.head.get_data()
        if self.head.get_next() is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        self._logger.debug(f"Removendo {value_removed} da lista; Estado atual da lista: {self.__str__()}")
        time.sleep(0.1)
        return value_removed

    def search(self, item: any) -> bool:
        if self.is_empty():
            self._logger.debug("Lista Vazia! Elementos não podem ser buscados!")
            time.sleep(0.1)
            return False
            # raise LinkedListVaziaException("Lista vazia!")

        curr = self.head
        while curr is not None:
            if curr.get_data() == item:
                self._logger.debug(f"Procurando {item} na lista; Encontrou? Sim; Estado atual da lista: {self.__str__()}")
                time.sleep(0.1)
                return True
            curr = curr.get_next()

        self._logger.debug(f"Procurando {item} na lista; Encontrou? Não; Estado atual da lista: {self.__str__()}")
        time.sleep(0.1)
        return False

    def __str__(self) -> str:
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.get_data()))
            curr = curr.get_next()
        return " => ".join(elements)
