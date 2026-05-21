class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            ch = s[i]
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (ch == ')' and top != '(') or \
                (ch == '}' and top != '{') or \
                (ch == ']' and top != '['):
                    return False
                stack.pop()
        
        return len(stack) == 0
