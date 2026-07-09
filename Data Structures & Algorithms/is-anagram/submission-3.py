class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapp = {}

        for i in s:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        
        for i in t:
            if i not in mapp:
                return False
            elif i in mapp:
                if mapp[i] == 0:
                    return False
                else:
                    mapp[i] -= 1
        return True
                