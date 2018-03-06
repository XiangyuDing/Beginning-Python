import threading
import time
from queue import Queue
import copy

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)

def mulithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target = job, args = (data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        result.append(q.get())
    print(result)

if __name__ == '__main__':
    mulithreading()
