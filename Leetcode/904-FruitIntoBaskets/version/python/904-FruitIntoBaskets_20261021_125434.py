# Last updated: 10/21/2026, 12:54:34 PM
1class Solution:
2    def totalFruit(self, fruits: list[int]) -> int:
3        seen = {}
4        left = 0
5        max_fruit = 0
6
7        for right in range(len(fruits)):
8            seen[fruits[right]] = seen.get(fruits[right], 0) + 1
9
10            while len(seen) > 2:
11                seen[fruits[left]] -= 1
12
13                if seen[fruits[left]] == 0:
14                    del seen[fruits[left]]
15
16                left += 1
17
18            max_fruit = max(max_fruit, right - left + 1)
19
20        return max_fruit