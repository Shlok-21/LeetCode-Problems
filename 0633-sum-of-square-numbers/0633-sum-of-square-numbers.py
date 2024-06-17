import numpy as np
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        flag = 0
        for a in range(int(np.sqrt(c)+1)):
            b = np.sqrt(c- a*a)
            if b == int(b):
                return True        
        if flag == 0: return False
        