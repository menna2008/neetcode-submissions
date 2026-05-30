class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        res = [0] * length
        for i in range(length - 2, -1, -1):
            temp = temperatures[i]
            j = i + 1

            while j < length and temperatures[j] <= temp:
                if res[j] == 0:
                    j = length
                else:
                    j += res[j]
            
            if j < length:
                res[i] = j - i
        
        return res
        