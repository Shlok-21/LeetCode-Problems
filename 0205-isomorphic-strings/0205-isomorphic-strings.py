class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_string = []
        t_string = []
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_string.append(s.index(s[i]))
            t_string.append(t.index(t[i]))
        
        return True if t_string == s_string else False
            
