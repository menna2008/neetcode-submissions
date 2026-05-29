class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        freq = {}
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1
        
        have = 0
        need = len(freq)

        res = ''
        min_length = float('inf')
        l = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in freq:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == freq[ch]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    res = s[l : r + 1]
                
                left_char = s[l]
                if left_char in freq:
                    if window[left_char] == freq[left_char]:
                        have -= 1
                    window[left_char] -= 1
                
                l += 1
        
        return res
        