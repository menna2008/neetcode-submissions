class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        
        curr.end = True

    def search(self, word: str) -> bool:
        stack = [(0, self.root)]

        while stack:
            i, curr = stack.pop()

            if i == len(word):
                if curr.end: return True
                continue

            if word[i] == '.':
                # explore every child
                next = i + 1
                for j in range(26):
                    if curr.children[j]:
                        stack.append((next, curr.children[j]))
            else:
                # explore only the matching child
                idx = ord(word[i]) - ord('a')
                if curr.children[idx] == None: continue
                stack.append((i + 1, curr.children[idx]))
        
        return False
