class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s1 = [x for x in s[::-1] if x.isalpha() == 1]
        print(s1)
        ans = []
        i=1
        for a in range(len(s)):
            if s[a].isalpha():
                ans.append(s1[0])
                s1.pop(0)
            else:
                ans.append(s[a])
        return ''.join(ans)