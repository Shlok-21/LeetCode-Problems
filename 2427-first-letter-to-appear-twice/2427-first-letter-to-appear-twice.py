class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = []
        for i in s:
            if i not in check:
                check.append(i)
            else:
                return i