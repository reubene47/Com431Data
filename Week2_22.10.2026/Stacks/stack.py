class Stack:
    def __init__(self):
        self.internal_list = []
    
    def push(self, item):
        self.internal_list.append(item)

        pass # ends the method when it's empty

    def pop(self):
        deleted = self.internal_list[-1]
        del self.internal_list[-1]
        return deleted
    
        pass # ends the method when it's empty

    def peek(self):
        return self.internal_list[-1]
    
    def __str__(self):
        return self.internal_list.__str__()