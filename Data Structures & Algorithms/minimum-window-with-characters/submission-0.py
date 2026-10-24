
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        compare = {}
        substring = {}
        shortest = float('inf')
        output = ""

        # find the frequency we need in the substring
        for letter in t:
            if letter in compare:
                compare[letter] += 1
            else:
                compare[letter] = 1

        left, right = 0, 0
        matches = 0

        while right < len(s):
            letter = s[right]

            if letter in compare:
                if letter in substring:
                    substring[letter] += 1
                else:
                    substring[letter] = 1

                if substring[letter] == compare[letter]:
                    matches += 1

            # shrink the window while it contains everything we need
            while matches == len(compare):
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    output = s[left:right + 1]

                left_letter = s[left]

                if left_letter in compare:
                    if substring[left_letter] == compare[left_letter]:
                        matches -= 1
                    substring[left_letter] -= 1

                left += 1

            right += 1

        return output