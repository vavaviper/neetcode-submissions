# Last updated: 10/20/2026, 2:50:36 AM
1class Solution:
2    def twoSum(self, nums: list[int], target: int) -> list[int]:
3        seen = {} #{number: index}
4        for n in range(len(nums)):
5            if (target - nums[n]) in seen:
6                return [n, seen[target - nums[n]]]
7            else:
8                seen[nums[n]] = n
9            
10