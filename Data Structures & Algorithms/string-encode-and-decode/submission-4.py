class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        ptr = 0
        while ptr < len(s):
            count = 0
            while s[ptr] != '#':
                count = count * 10 + int(s[ptr])
                ptr += 1
            res.append(s[ptr + 1 : ptr + count + 1])
            ptr += 1 + count
        return res
