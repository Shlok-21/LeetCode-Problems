class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s_checker = ''
        for i in words:
            s_checker += i[0]
        return s_checker == s