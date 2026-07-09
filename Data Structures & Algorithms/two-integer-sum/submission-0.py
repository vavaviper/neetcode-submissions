class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = set()

        for i in range(len(nums)):
            check = target - nums[i]
            if check in mapp:
                return sorted([i, nums.index(check)])
            mapp.add(nums[i])