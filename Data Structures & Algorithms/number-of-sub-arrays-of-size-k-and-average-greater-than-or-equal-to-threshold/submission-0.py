class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum = 0
        for i in range(k):
            sum += arr[i]
        
        if (sum / k) >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            sum = sum + arr[i] - arr[i - k]
            if sum / k >= threshold:
                count += 1
        
        return count
        