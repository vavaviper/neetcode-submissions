class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = set()
        for i in nums:
            if i in mapp:
                return True
            else:
                mapp.add(i)

        return False