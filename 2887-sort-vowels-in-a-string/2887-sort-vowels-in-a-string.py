class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        ords = []
        for i in s:
            if i.lower() in vowels:
                ords.append(ord(i))
        ords.sort()
        ans = []
        vowel_pointer = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                ans.append(chr(ords[vowel_pointer]))
                vowel_pointer+=1
            else:
                ans.append(s[i])
        return ''.join(ans) 