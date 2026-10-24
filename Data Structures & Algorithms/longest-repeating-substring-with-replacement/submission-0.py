class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        output = 0
        seen = {}

        while right < len(s):
            #move right pointer, add new char into dictionary
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1

            #find most repeating char
            max_val = max(seen.values())

            #check if that (right-left) - freq > k
            if (right - left + 1 - max_val) > k:
                #if yeah max(output, right-left)
                
            
                #if not, remove the left pointer from seen and left += 1
                seen[s[left]] -= 1
                left += 1
            output = max(output, right-left+1)
            right += 1
        return output

