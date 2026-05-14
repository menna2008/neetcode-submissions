class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in dictionary:
                return [dictionary[difference], i]
            
            dictionary[nums[i]] = i
        