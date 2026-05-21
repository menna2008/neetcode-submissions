class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if (s[i] == ')' and stack[-1] != '(') or \
                (s[i] == '}' and stack[-1] != '{') or \
                (s[i] == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        
        return len(stack) == 0
