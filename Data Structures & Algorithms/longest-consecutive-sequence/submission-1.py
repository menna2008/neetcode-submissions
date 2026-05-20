class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = 1
        nums = set(nums)
        for num in nums:
            streak = 1
            if (num - 1) in nums:
                continue
            while (num + streak) in nums:
                streak += 1
            res = max(res, streak)
        
        return res
        