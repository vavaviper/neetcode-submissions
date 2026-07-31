class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
                return True
        store = set()
        output = 0
        while n != 1:
            if n not in store:
                store.add(n)
                n = self.check(n)
            elif n in store:
                return False
            if n == 1:
                return True
        return False
                
    def check(self, n):
        print(n)
        output = 0
        for i in str(n):
            output += (int(i) ** 2)
        return output
