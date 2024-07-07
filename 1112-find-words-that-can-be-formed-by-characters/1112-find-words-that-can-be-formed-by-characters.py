class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = list(chars)
        total = 0
        temp_chars = chars.copy()
        for word in words:
            flag = True
            for char in word:
                if char in temp_chars:
                    temp_chars.remove(char)
                else:
                    flag = False
            temp_chars = chars.copy()
            if flag == True:
                total += len(word)
        return total