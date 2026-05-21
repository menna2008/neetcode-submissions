class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0; r = len(heights) - 1
        maxim = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            maxim = max(maxim, water)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxim
        