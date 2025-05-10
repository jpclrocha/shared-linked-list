from threading import Thread
from linked_list import LinkedList, LinkedListVaziaException
from custom_logger import get_logger
import random
from math import floor

logger = get_logger()
lista = LinkedList()

def worker_append():
    global lista
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.append(value)
        logger.debug(f"Adicionando {value} na lista; Estado atual da lista: {lista}")

def worker_pop():
    global lista
    for _ in range(0, 60):
        try:
            logger.debug(f"Removendo {lista.pop()} da lista; Estado atual da lista: {lista}")
        except LinkedListVaziaException:
            logger.debug("Lista Vazia! Elementos não podem ser removidos!")
        
def worker_search():
    global lista
    for _ in range(0, 50):
        try:
            value = floor(random.random() * 10)
            logger.debug(f"Procurando {value} na lista; Encontrou? {'Sim' if lista.search(value) else 'Não'}; Estado atual da lista: {lista}")
        except LinkedListVaziaException:
            logger.debug("Lista Vazia! Elementos não será encontrado!")

# create threads
t1 = Thread(target=worker_append, name="ADD-1")
t2 = Thread(target=worker_append, name="ADD-2")
t3 = Thread(target=worker_pop, name="POP-1")
t4 = Thread(target=worker_pop, name="POP-2")
t5 = Thread(target=worker_search, name="BUSCA")

# start the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# wait for the threads to complete
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print(lista)
