from threading import Thread
from linked_list_lock import LinkedListLock
import random
from math import floor
import time

lista = LinkedListLock()

def worker_append():
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.append(value)
        time.sleep(0.0001)

def worker_pop():
    for _ in range(0, 50):
        lista.pop()
        time.sleep(0.0001)
        
def worker_search():
    for _ in range(0, 50):
        value = floor(random.random() * 10)
        lista.search(value)
        time.sleep(0.0001)

# criar múltiplas threads de cada tipo
threads: list[Thread] = []

for i in range(2):
    threads.append(Thread(target=worker_search, name=f"BUSCA-{i+1}"))
    threads.append(Thread(target=worker_append, name=f"ADD-{i+1}"))
    threads.append(Thread(target=worker_pop, name=f"POP-{i+1}"))

for thread in threads:
    thread.start()
    
for thread in threads:
    thread.join()

print(f"Total final na lista (agr com lock): {lista.size()}")