class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        for i in range(1, len(nums)):
            products[i] = products[i - 1] * nums[i - 1]
        
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            products[i] *= prod
        
        return products

        