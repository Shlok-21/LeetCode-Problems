from collections import Counter, defaultdict
class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        checker = sorted(set(s))
        
        char_count = defaultdict(int)
        for i in s:
            char_count[i] += 1

        
        while char_count:
            for i in checker:
                if char_count[i]>0:
                    char_count[i] -= 1
                    res+= str(i)
                else:
                    del char_count[i]
                    
            for i in checker[::-1]:
                if char_count[i]>0:
                    char_count[i] -= 1
                    res+= str(i)
                else:
                    del char_count[i]        
        return res