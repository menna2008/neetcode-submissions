class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            element = nums[mid]
            if element == target:
                return mid
            elif element > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
        