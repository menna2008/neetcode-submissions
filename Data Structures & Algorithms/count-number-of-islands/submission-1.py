class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0

        stack = []

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    stack.append((row, col))
                    num_islands += 1

                    while stack:
                        r, c = stack.pop()
                        if (r < 0 or r >= ROWS
                        or c < 0 or c >= COLS
                        or grid[r][c] == '0'):
                            continue
                        
                        grid[r][c] = '0'
                        stack.append((r + 1, c))
                        stack.append((r - 1, c))
                        stack.append((r, c + 1))
                        stack.append((r, c - 1))

        return num_islands
        