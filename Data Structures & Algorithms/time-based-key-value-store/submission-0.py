class TimeMap:
    def __init__(self):
        self.struct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.struct:
            self.struct[key] = []
        self.struct[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.struct: return ""
        
        ls = self.struct[key]
        left, right = 0, len(ls) - 1
        answer = ''

        while left <= right:
            mid = left + (right - left) // 2

            if ls[mid][0] <= timestamp:
                answer = ls[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return answer

