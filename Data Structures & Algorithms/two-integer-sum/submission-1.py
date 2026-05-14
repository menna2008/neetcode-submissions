class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[n] = i
        