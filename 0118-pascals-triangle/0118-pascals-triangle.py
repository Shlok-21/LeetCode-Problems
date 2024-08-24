from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        i = 1
        if numRows == 1:
            return ans
        else:
            i+=1
            while i <= numRows:
                middle = []
                for j in range(len(ans[-1])-1):
                    middle.append(ans[-1][j]+ans[-1][j+1])
                ans_next = [1]
                for z in middle:
                    ans_next.append(z)
                ans_next.append(1)
                i+=1
                ans.append(ans_next)                
            return ans                