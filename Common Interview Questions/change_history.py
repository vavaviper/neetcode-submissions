'''
Change History

You are building a system that tracks the value of configuration settings over time.

Implement a ChangeHistory class with the following methods:

set(key, value, timestamp)

Stores value for key at the given timestamp.

key is a string.
value is a string.
timestamp is an integer.
Timestamps provided for the same key are strictly increasing.
get(key, timestamp)

Returns the value associated with key at the most recent timestamp less than or equal to timestamp.

If no value exists for key at or before the given timestamp, return "".

Input Format

The system receives a sequence of operations.

Each operation is one of:

SET key value timestamp
GET key timestamp
Output Format

For every GET operation, print the corresponding value on its own line.

Example

Input

SET theme dark 1
SET theme light 5
SET theme system 10
GET theme 1
GET theme 4
GET theme 7
GET theme 15
GET language 3

Output

dark
dark
light
system

Constraints
1 <= number of operations <= 100,000
1 <= timestamp <= 10^9
Keys and values contain only lowercase English letters.
SET timestamps for a given key are strictly increasing.
'''

class ChangeHistory:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = {}
        history = self.store[key]
        history[timestamp] = value

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        history = self.store[key]
        if timestamp in history:
            return history[timestamp]
        else:
            keys = list(history.keys())

            if timestamp < keys[0]:
                return ""

            left = 0
            right = len(keys) - 1

            answer = 0
            while left <= right:
                mid = (left + right) // 2

                if keys[mid] <= timestamp:
                    answer = keys[mid]
                    left = mid + 1
                else:
                    right = mid -1
            
        return history[answer]

# Test 1: Basic exact matches
history = ChangeHistory()

history.set("theme", "dark", 1)
history.set("theme", "light", 5)
history.set("theme", "system", 10)

print(history.get("theme", 1))   # Expected: "dark"
print(history.get("theme", 5))   # Expected: "light"
print(history.get("theme", 10))  # Expected: "system"

# Test 2: Timestamp between two values
history = ChangeHistory()

history.set("theme", "dark", 1)
history.set("theme", "light", 5)
history.set("theme", "system", 10)

print(history.get("theme", 7))   # Expected: "light"
print(history.get("theme", 9))   # Expected: "light"