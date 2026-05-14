class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        values = {}
        while i < len(nums):
            if nums[i] in nums[ : i]:
                return True
            i += 1
        return False
        