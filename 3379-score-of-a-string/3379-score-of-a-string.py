class Solution:
    def scoreOfString(self, s: str) -> int:
        sums= 0
        for index in range(len(s)-1):
            sums += (abs(ord(s[index]) - ord(s[index+1])))
        return sums  