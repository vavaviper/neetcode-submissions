# Last updated: 10/24/2026, 9:59:25 AM
1class RandomizedSet:
2
3    def __init__(self):
4        self.set = set()
5        self.lst = []
6
7    def insert(self, val: int) -> bool:
8        if val in self.set:
9            return False
10        else:
11            self.set.add(val)
12            self.lst.append(val)
13            return True
14        
15
16    def remove(self, val: int) -> bool:
17        if val not in self.set:
18            return False
19        else:
20            self.set.remove(val)
21            self.lst.remove(val)
22            return True
23
24    def getRandom(self) -> int:
25        return random.choice(self.lst)
26
27
28
29# Your RandomizedSet object will be instantiated and called as such:
30# obj = RandomizedSet()
31# param_1 = obj.insert(val)
32# param_2 = obj.remove(val)
33# param_3 = obj.getRandom()