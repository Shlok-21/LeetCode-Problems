class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good = 0
        for i in range(len(s)-2):
            seet = s[i:i+3]
            if len(seet) == len(set(seet)):
                good += 1

        return good