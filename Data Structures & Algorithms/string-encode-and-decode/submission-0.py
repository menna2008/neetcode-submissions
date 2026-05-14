class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}%{s}")
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        i = 0
        arr = []
        while i < len(s):
            length = s[i]
            while s[i + 1] != '%':
                i += 1
                length += s[i]
            string = s[i + 2 : i + 2 + int(length)]
            arr.append(string)
            i += 2 + int(length)
        return arr
