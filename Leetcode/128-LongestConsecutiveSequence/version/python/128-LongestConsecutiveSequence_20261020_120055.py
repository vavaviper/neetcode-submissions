# Last updated: 10/20/2026, 12:00:55 PM
1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        seen = set(nums)
4        max_consec = 0
5
6        for num in seen:
7            if num - 1 not in seen:
8                curr = 1
9                n = num
10
11                while n + 1 in seen:
12                    curr += 1
13                    n += 1
14
15                if curr > max_consec:
16                    max_consec = curr
17
18        return max_consec