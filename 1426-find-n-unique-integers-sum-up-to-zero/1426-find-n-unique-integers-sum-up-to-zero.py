class Solution:
    def sumZero(self, n: int):
        ans = []
        if n%2 == 1:
            ans.append(0)
        for i in range(1,int(n/2+1)):
            print(i)
            ans.append(i)        
            ans.append(-i)        
        return ans   