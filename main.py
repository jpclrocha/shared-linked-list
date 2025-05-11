from threading import Thread
from linked_list import LinkedList, LinkedListVaziaException
import random
from math import floor
import time

lista = LinkedList()

def worker_append():
    global lista
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.append(value)
        time.sleep(0.0001)

def worker_pop():
    global lista
    for _ in range(0, 50):
        lista.pop()
        time.sleep(0.0001)
        
def worker_search():
    global lista
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.search(value)
        time.sleep(0.0001)

# criar múltiplas threads de cada tipo
threads = []

for i in range(2):
    threads.append(Thread(target=worker_append, name=f"ADD-{i+1}"))
    threads.append(Thread(target=worker_pop, name=f"POP-{i+1}"))
    threads.append(Thread(target=worker_search, name=f"BUSCA-{i+1}"))

# iniciar todas
for t in threads:
    t.start()

# aguardar término
for t in threads:
    t.join()

print(f"Total final na lista (não confiável sem lock): {lista.size()}")