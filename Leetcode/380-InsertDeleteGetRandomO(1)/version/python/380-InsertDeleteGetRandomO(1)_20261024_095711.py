# Last updated: 10/24/2026, 9:57:11 AM
1class RandomizedSet:
2
3    def __init__(self):
4        self.set = set()
5
6    def insert(self, val: int) -> bool:
7        if val in self.set:
8            return False
9        else:
10            self.set.add(val)
11            return True
12        
13
14    def remove(self, val: int) -> bool:
15        if val not in self.set:
16            return False
17        else:
18            self.set.remove(val)
19            return True
20
21    def getRandom(self) -> int:
22        return random.choice(list(self.set))
23
24
25
26# Your RandomizedSet object will be instantiated and called as such:
27# obj = RandomizedSet()
28# param_1 = obj.insert(val)
29# param_2 = obj.remove(val)
30# param_3 = obj.getRandom()