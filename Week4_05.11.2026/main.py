import hash_table
from linkedlist import TuplesLinkedList
from hash_table import HashTable

hash_table = HashTable()

hash_table.put("address", "123 Main St")

print(hash_table.get("address"))