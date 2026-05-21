class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i in range(len(s)):
            ch = s[i]
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack) == 0 or mapping[ch] != stack[-1]:
                    return False
                stack.pop()
        
        return len(stack) == 0
