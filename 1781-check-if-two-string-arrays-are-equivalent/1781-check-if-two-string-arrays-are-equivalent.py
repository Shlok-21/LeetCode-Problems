class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        '''s1 = ''
        s2 = ''
        for word in word1:
            s1+= ''.join(word)
        for word in word2:
            s2+= ''.join(word)
        if s1 == s2:
            return True
        else:
            return False'''