from linkedlist import TuplesLinkedList

# initialise list
linked_list = TuplesLinkedList()

# create HashTable class
class HashTable:
    def __init__(self, size=17):
        self.size = size
        self.buckets = [TuplesLinkedList() for i in range(size)]

    def get(self, key):
        hash = self.calc_hash_code(key)
        return linked_list[self.buckets].find(hash)

    def put(self, key, value):
        hash = self.calc_hash_code(key)
        linked_list[self.buckets].add(hash, value)

    def calc_hash_code(self, key):
        hash_total = 0

        for character in key:
            hash_total = hash_total + ord(character)