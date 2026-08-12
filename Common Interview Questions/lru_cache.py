'''
LRU Cache

You are building a cache that stores key-value pairs. The cache has a fixed capacity. When the cache is full and a new item needs to be added, the least recently used item must be removed.

Implement an LRUCache class with the following operations:

LRUCache(capacity)
get(key)
put(key, value)
Requirements
get(key) returns the value associated with key.
If key does not exist, get should return -1.
put(key, value) adds or updates the key-value pair.
Accessing a key with get makes it the most recently used key.
Updating a key with put also makes it the most recently used key.
If adding a new key causes the cache to exceed its capacity, remove the least recently used key.
Both get and put should run in O(1) average time.
Example
LRUCache cache = new LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

cache.get(1)       → 10

cache.put(3, 30)   // key 2 is now least recently used

cache.get(2)       → -1

cache.get(3)       → 30
Another example
LRUCache cache = new LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

cache.get(1)       → 10
cache.put(3, 30)

cache.get(1)       → 10
cache.get(2)       → -1
cache.get(3)       → 30
'''

class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.lru = None

    def get(self, key):
        if key in self.store:
            self.lru = key
            print("lru:",self.lru)
            return self.store[key]
        else:
            return -1

    def put(self, key, value):
        print("store", self.store)
        
        if len(self.store.values()) == self.capacity:
            del self.store[self.lru]
            print("deleted", self.lru)
        self.store[key] = value
        self.lru = key
        print("lru:",self.lru)


cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))#       → 10

cache.put(3, 30)  # // key 2 is now least recently used

print(cache.get(2))#    → -1

print(cache.get(3))     #→ 30