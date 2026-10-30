class Queue:

    def __init__(self, capacity):
        self.internal_array = [None] * capacity
        self.front = 0
        # next available index
        self.back = 0
        self.size = 0

    def add(self, item):
        if self.size == len(self.internal_array):
            print("Queue is full")
        else:
            self.internal_array[self.back] = item
            self.back = (self.back + 1) % len(self.internal_array)
            self.size += 1


    def remove(self):
        if self.size == 0:
            print("Queue is empty")
        item = self.internal_array[self.front]
        self.internal_array[self.front] = None
        self.front = (self.front + 1) % len(self.internal_array)
        self.size -= 1
        return item

    def __str__(self):
        return self.internal_array.__str__()