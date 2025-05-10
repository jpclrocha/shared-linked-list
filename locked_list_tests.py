from threading import Thread
from linked_list_lock import LinkedListLock, LinkedListVaziaException
from custom_logger import get_logger
import random
from math import floor
import time

logger = get_logger()
lista = LinkedListLock()

def worker_append():
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.append(value)
        logger.debug(f"Adicionando {value} na lista; Estado atual da lista: {lista}")
        time.sleep(0.0001)

def worker_pop():
    for _ in range(0, 40):
        try:
            logger.debug(f"Removendo {lista.pop()} da lista; Estado atual da lista: {lista}")
        except LinkedListVaziaException:
            logger.debug("Lista Vazia! Elementos não podem ser removidos!")
        time.sleep(0.0001)
        
def worker_search():
    for _ in range(0, 50):
        try:
            value = floor(random.random() * 10)
            logger.debug(f"Procurando {value} na lista; Encontrou? {'Sim' if lista.search(value) else 'Não'}; Estado atual da lista: {lista}")
        except LinkedListVaziaException:
            logger.debug("Lista Vazia! Elementos não será encontrado!")
        time.sleep(0.0001)

# criar múltiplas threads de cada tipo
threads = []

for i in range(10):
    threads.append(Thread(target=worker_append, name=f"ADD-{i+1}"))
    threads.append(Thread(target=worker_pop, name=f"POP-{i+1}"))
    threads.append(Thread(target=worker_search, name=f"BUSCA-{i+1}"))

# iniciar todas
for t in threads:
    t.start()

# aguardar término
for t in threads:
    t.join()

print(f"Total final na lista (agr com lock): {lista.size()}")