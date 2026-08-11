'''
In-Memory Key-Value Store

You are building a simple in-memory key-value store that allows applications to store and retrieve data using unique keys.

Implement a KeyValueStore class with the following operations:

set(key, value)
get(key)
delete(key)
Requirements
key is a string.
value can be any value.
Each key can have at most one value associated with it.
Calling set on an existing key should overwrite its previous value.
get should return the value associated with the key.
If the key does not exist, get should return None.
delete should remove the key if it exists.
Deleting a key that does not exist should do nothing.
Example
store.set("name", "Varsha")
store.set("age", 21)

store.get("name")       → "Varsha"
store.get("age")        → 21
store.get("school")     → None

store.set("age", 22)
store.get("age")        → 22

store.delete("name")
store.get("name")       → None
Your task

'''

class KeyValueStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value

    def get(self, key):
        if key in self.store:
            return self.store[key]
        return None

    def delete(self, key):
        if key in self.store:
            del self.store[key]
        

store = KeyValueStore()
store.set("name", "Varsha")
store.set("age", 21)

print(store.get("name"))     # → "Varsha"
print(store.get("age"))       # → 21
print(store.get("school"))    # → None

store.set("age", 22)
print(store.get("age"))    # → 22

store.delete("name")
print(store.get("name")) 
