class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window = {}

        # frequency map for s1
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        # initial window
        for c in s2[:len(s1)]:
            window[c] = window.get(c, 0) + 1

        if window == s1_count:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            # add new character
            window[s2[right]] = window.get(s2[right], 0) + 1

            # remove old character
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            if window == s1_count:
                return True

        return False