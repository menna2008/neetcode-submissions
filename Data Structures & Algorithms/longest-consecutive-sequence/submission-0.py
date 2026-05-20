class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        res = 0
        nums.sort()

        streak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == (nums[i - 1] + 1):
                streak += 1
            else:
                res = max(res, streak)
                streak = 1

        return max(res, streak)
        