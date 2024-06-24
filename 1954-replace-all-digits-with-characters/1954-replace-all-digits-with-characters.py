class Solution:
    def replaceDigits(self, s: str) -> str:
        new = ''
        for i in range(len(s)):
            if s[i].isnumeric():
                new += str(chr(ord(s[i-1])+int(s[i])))
            else:
                new += s[i]
        return new