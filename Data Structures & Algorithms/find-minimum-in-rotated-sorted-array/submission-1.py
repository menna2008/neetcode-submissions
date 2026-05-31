class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i + 1]:
                return nums[i + 1]
        
        if i == len(nums) - 1: return nums[0]
        