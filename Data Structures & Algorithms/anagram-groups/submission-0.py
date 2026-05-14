class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            ordered = ''.join(sorted(string))
            if ordered in dictionary:
                dictionary[ordered].append(string)
            else:
                dictionary[ordered] = [string]
        
        ls = []
        for value in dictionary.values():
            ls.append(value)
        return ls
        