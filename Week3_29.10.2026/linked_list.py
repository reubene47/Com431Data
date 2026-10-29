from node import Node

class LinkedList:

    # initialise the linked list
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    # add an item to the linked list
    def add(self, item):
        node = Node(item)

        # if list is empty
        if self.last is None:
            self.first = node
            self.last = node

        else:
            node.previous = self.last
            node.next = None

            self.last.next = node
            self.last = node

        self.size += 1

    def get(self, index):
        item = self.first

        # work forwards if index is closer to the front of linked list
        if index < 0 or index >= self.size:
            return None
        elif index < (self.size // 2):
            print("Starting from front of list")
            for i in range(index):
                item = item.next
            return item
        else:
            print("Starting from back of list")