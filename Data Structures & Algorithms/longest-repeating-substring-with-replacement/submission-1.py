class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        max_len = 0

        for char in chars:
            non_chars = 0
            l = 0

            for r in range(len(s)):
                if s[r] != char:
                    non_chars += 1
                
                while non_chars > k:
                    if s[l] != char:
                        non_chars -= 1
                    l += 1
                max_len = max(max_len, r - l + 1)
        
        return max_len
        