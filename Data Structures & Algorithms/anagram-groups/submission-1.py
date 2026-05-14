class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for character in string:
                count[ord(character) - ord('a')] += 1
            dictionary[tuple(count)].append(string)
        return list(dictionary.values())
        