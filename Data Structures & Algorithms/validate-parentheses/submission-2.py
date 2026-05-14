class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                elif hashmap[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        