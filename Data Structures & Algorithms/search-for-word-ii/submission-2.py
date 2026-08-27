class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.refs = 0
        self.word = -1
    
    def add_word(self, word, i):
        curr = self
        curr.refs += 1
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
            curr.refs += 1
        curr.word = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i, word in enumerate(words):
            root.add_word(word, i)

        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        res = []

        def dfs(row, col, node):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS
            or board[row][col] == '*'
            or not node.children[ord(board[row][col]) - ord('a')]):
                return 0
            
            found = 0
            temp = board[row][col]
            board[row][col] = '*'
            prev = node
            node = node.children[ord(temp) - ord('a')]
            if node.word != -1:
                res.append(words[node.word])
                node.word = -1
                found += 1
            
            found += dfs(row + 1, col, node)
            found += dfs(row - 1, col, node)
            found += dfs(row, col + 1, node)
            found += dfs(row, col - 1, node)

            board[row][col] = temp
            node.refs -= found

            if not node.refs:
                prev.children[ord(temp) - ord('a')] = None

            return found
        
        for row in range(ROWS):
            for col in range(COLS):
                root.refs -= dfs(row, col, root)

        return res
        