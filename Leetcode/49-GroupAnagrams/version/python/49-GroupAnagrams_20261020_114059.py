# Last updated: 10/20/2026, 11:40:59 AM
1class Solution:
2    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
3        groups = {}
4
5        for word in strs:
6            count = [0] * 26
7
8            for char in word:
9                count[ord(char) - ord('a')] += 1
10
11            key = tuple(count)
12
13            if key not in groups:
14                groups[key] = []
15
16            groups[key].append(word)
17
18        return list(groups.values())