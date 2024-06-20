class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.lower()
        brokenLetters = brokenLetters.lower()
        count = 0
        text = text.split(' ')

        for i in text:
            flag = 0
            for j in brokenLetters:
                if j in i:
                    flag =1

            if flag == 0:
                count +=1

        return count