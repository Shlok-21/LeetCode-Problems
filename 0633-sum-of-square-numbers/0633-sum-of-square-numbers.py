import numpy as np
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        flag = 0
        for a in range(1, int(np.sqrt(c)+1)):
            b = np.sqrt(c- a*a)
            if b == int(b):
                flag = 1
                
        if flag == 0: return False
        else : return True