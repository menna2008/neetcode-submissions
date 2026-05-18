class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = (i // 3) * 3 + (j // 3)
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rows[i]:
                    return False
                elif board[i][j] in cols[j]:
                    return False
                elif board[i][j] in squares[cell]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[cell].add(board[i][j])
        
        return True
