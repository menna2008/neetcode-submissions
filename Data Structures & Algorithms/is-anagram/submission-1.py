from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t) 
        '''
        Counter converts s to a dictionary where 
        the keys are the distinct characters and 
        the values are the number of times the character appears
        ''' 