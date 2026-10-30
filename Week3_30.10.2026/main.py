from queue import Queue

# Create a queue with 5 capacity
queue1 = Queue(5)

queue1.add(4); queue1.add(2); queue1.add(3)

print(queue1)

print(queue1.remove())

print(queue1)