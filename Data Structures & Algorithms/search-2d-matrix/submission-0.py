class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        left_row, right_row = 0, rows - 1
        while left_row <= right_row:
            mid = left_row + (right_row - left_row) // 2
            if matrix[mid][0] <= target <= matrix[mid][columns - 1]:
                break
            elif target < matrix[mid][0]:
                right_row = mid - 1
            else:
                left_row = mid + 1
        
        row = matrix[mid]
        left, right = 0, columns - 1
        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        