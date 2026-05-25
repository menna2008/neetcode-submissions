class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        seen = {s[0]}
        l, r = 0, 1
        max_length = 0

        while r < len(s):
            curr = s[r]
            if curr not in seen:
                seen.add(curr)
            else:
                max_length = max(max_length, r - l)
                while curr in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(curr)
            
            r += 1
        
        return max(max_length, r - l)
        