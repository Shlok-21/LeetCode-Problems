class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        for i in range(len(s) -1):
            print(ord(s[i+1]) - ord(s[i]))
            if abs(ord(s[i+1]) - ord(s[i])) != 32 and (abs(ord(s[i+1]) - ord(s[i]))) != 0:
                count +=1
        return count