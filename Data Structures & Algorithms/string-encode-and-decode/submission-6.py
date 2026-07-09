class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return str([])
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == '[]':
            return []
        strs = []
        i = 0

        if s == '':
            return ''
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            strs.append(s[i:i + length])
            i += length
        return strs
                
