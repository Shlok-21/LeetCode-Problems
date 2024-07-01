class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        def checker(s, part):
            if part in s:
                l_index = s.index(part)
                r_index = l_index + len(part)
                s = s[:l_index] + s[r_index:]
                return checker(s, part)
            else:
                return s

        return checker(s, part)    