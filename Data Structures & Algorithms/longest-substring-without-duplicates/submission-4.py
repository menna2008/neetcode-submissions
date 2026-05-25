class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        seen = {s[0] : 0}
        l, r = 0, 1
        max_length = 0

        while r < len(s):
            curr = s[r]
            
            if curr in seen and seen[curr] >= l:
                max_length = max(max_length, r - l)
                l = seen[curr] + 1
            
            seen[curr] = r
            r += 1
        
        return max(max_length, r - l)
        