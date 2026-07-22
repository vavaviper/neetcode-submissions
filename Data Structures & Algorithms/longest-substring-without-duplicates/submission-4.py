class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        repeat = {s[0]}
        left = 0
        right = 1
        max_count = 1

        while right < len(s):
            if s[right] in repeat:
                repeat.remove(s[left])
                left += 1
            else:
                repeat.add(s[right])
                right += 1
                max_count = max(right - left, max_count)
        return max_count
