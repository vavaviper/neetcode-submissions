'''
Smart Resource Store

You are building a resource store that keeps a limited number of items in memory.

Each item has a unique integer key and an associated integer value. The store has a fixed capacity.

Implement a class called ResourceStore with the following operations:

ResourceStore(capacity)

Initializes the store with the given maximum capacity.

get(key)

Returns the value associated with key.

If key does not exist in the store, return -1.

Every time an existing key is accessed, its access count increases by 1.

put(key, value)

Adds or updates an item.

If key already exists, update its value and increase its access count by 1.
If key does not exist and the store is at capacity, remove the item that has been accessed the fewest number of times before inserting the new item.
If multiple items have the same access count, remove the item that was least recently accessed among them.
A newly inserted item starts with an access count of 1.
Requirements

Implement:

ResourceStore(capacity)
get(key)
put(key, value)
Example
Input:
ResourceStore(2)

put(1, 10)
put(2, 20)
get(1)
put(3, 30)
get(2)
get(3)

Output:
10
-1
30

Constraints

1 <= capacity <= 10^5
1 <= key <= 10^9
-10^9 <= value <= 10^9
Up to 2 * 10^5 operations

Important: Your implementation should be efficient enough to handle the maximum constraints.
'''


class ResourceStore:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = {}
        self.freq = {}
        self.accessed = {}
        self.access_id = 1

    def get(self,key):
        # Return value if present and update its frequency + recency
        if key in self.store:
            # increment access count and update recency timestamp
            self.freq[key] = self.freq.get(key, 0) + 1
            self.accessed[key] = self.access_id
            self.access_id += 1
            return self.store[key]
        return -1

    def put(self, key, value):
        # If capacity is 0 do nothing
        if self.capacity <= 0:
            return

        # If key already exists, update value and count as an access
        if key in self.store:
            self.store[key] = value
            self.freq[key] = self.freq.get(key, 0) + 1
            self.accessed[key] = self.access_id
            self.access_id += 1
            return

        # If at capacity, evict one key: least frequency, then least recently accessed
        if len(self.store) >= self.capacity:
            # find minimum frequency
            mini = min(self.freq.values())
            # candidates with that frequency
            keys = [k for k, v in self.freq.items() if v == mini]
            if len(keys) == 1:
                victim = keys[0]
            else:
                # tie-breaker: remove least recently accessed (smallest timestamp)
                victim = min(keys, key=lambda k: self.accessed.get(k, 0))

            # remove victim from all maps
            del self.store[victim]
            del self.freq[victim]
            del self.accessed[victim]

        # Insert new key with initial access count = 1 and current timestamp
        self.store[key] = value
        self.freq[key] = 1
        self.accessed[key] = self.access_id
        self.access_id += 1


    def access(self, key):
        # Helper retained for compatibility but not used by main logic anymore.
        # It safely increments frequency and updates recency for an existing key.
        if key in self.store:
            self.freq[key] = self.freq.get(key, 0) + 1
            self.accessed[key] = self.access_id
            self.access_id += 1
            return self.store[key]
        # If key not present, do nothing (avoid creating entries for non-existent keys)
        return None


store = ResourceStore(2)

store.put(1, 10)
store.put(2, 20)
# Print results so script outputs the example expected values.
print(store.get(1))  # expected 10
store.put(3, 30)
print(store.get(2))  # expected -1 (evicted)
print(store.get(3))  # expected 30
