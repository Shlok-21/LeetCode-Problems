class Solution:

    def check_pattern(self, string):
        map1 = []
        for i in string:
            map1.append(string.index(i))
        return map1

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern = (self.check_pattern(pattern))
        matching = []
        for i in words:
            if self.check_pattern(i) == pattern:
                matching.append(i)     
        return matching