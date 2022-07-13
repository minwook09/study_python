import queue

data_queue = queue.Queue()
data_queue.put(1)
data_queue.put(2)
data_queue.put(3)
print(data_queue.get()) #1출력
print(data_queue.get()) #2출력

data_queue = queue.LifoQueue() #stack과 비슷
data_queue.put(1)
data_queue.put(2)
print(data_queue.get()) #2출력
print(data_queue.get()) #1출력

data_queue = queue.PriorityQueue() #데이터에 우선순위
data_queue.put((10, 1)) # (10,1)
data_queue.put((5, 2)) # (5, 2) - (10,1)
data_queue.put((15, 3)) # (5, 2) - (10, 1) - (15,3)
print(data_queue.get()) # (5,2) 출력
print(data_queue.get()) # (10, 1) 출
 