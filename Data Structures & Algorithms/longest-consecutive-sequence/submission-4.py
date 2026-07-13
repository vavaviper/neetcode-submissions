class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        count = 1
        max_streak = 1
        for i in nums:
            if i - 1 not in nums:
                count = 1
                while i + count in nums:
                    count += 1
                max_streak = max(count, max_streak)
        return max_streak