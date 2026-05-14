class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for string in strs:
            s += str(len(string)) + "#" + string
        
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            length = 0
            while s[i] != "#":
                length = length * 10 + int(s[i])
                i += 1
            i += 1
            strs.append(s[i : i + length])

            i += length
        
        return strs
