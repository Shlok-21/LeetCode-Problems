class Solution:
    def squareIsWhite(self, s: str) -> bool:
        if (int(ord(s[0])) % 2 == 1) and int(s[1])%2 == 1:
            return False
        elif (int(ord(s[0])) % 2 == 1) and int(s[1])%2 == 0:
            return True
        elif (int(ord(s[0])) % 2 == 0) and int(s[1])%2 == 1:
            return True
        elif (int(ord(s[0])) % 2 == 0) and int(s[1])%2 == 0:
            return False