class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        
        counts = {}

        for i in range(len_s):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1
        
        for value in counts.values():
            if value != 0:
                return False
        
        return True
        