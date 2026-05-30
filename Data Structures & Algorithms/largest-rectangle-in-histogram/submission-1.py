class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        right = [length - 1] * length
        left = [0] * length

        stack = []
        for i in range(length):
            while stack and heights[i] < stack[-1][0]:
                right[stack[-1][1]] = i - 1
                stack.pop()
            stack.append((heights[i], i))
        
        while len(stack) != 0:
            right[stack[-1][1]] = length - 1
            stack.pop()
        
        for j in range(length - 1, -1, -1):
            while stack and heights[j] < stack[-1][0]:
                left[stack[-1][1]] = j + 1
                stack.pop()
            stack.append((heights[j], j))
        
        while len(stack) != 0:
            left[stack[-1][1]] = 0
            stack.pop()
        
        res = 0
        for i in range(length):
            area = heights[i] * (right[i] - left[i] + 1)
            res = max(res, area)
        
        return res
        