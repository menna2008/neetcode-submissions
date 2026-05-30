class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack[-1][1]
                res[idx] = i - idx
                stack.pop()
            stack.append([temp, i])
        
        return res    
        