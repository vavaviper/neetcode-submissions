# Last updated: 10/24/2026, 10:00:34 AM
1import random
2
3class RandomizedSet:
4
5    def __init__(self):
6        self.lst = []
7        self.idx_map = {}
8
9    def search(self, val):
10        return val in self.idx_map
11
12    def insert(self, val):
13        if self.search(val):
14            return False
15
16        self.lst.append(val)
17        self.idx_map[val] = len(self.lst) - 1
18        return True
19
20    def remove(self, val):
21        if not self.search(val):
22            return False
23
24        idx = self.idx_map[val]
25        self.lst[idx] = self.lst[-1]
26        self.idx_map[self.lst[-1]] = idx
27        self.lst.pop()
28        del self.idx_map[val]
29        return True
30
31    def getRandom(self):
32        return random.choice(self.lst)
33
34