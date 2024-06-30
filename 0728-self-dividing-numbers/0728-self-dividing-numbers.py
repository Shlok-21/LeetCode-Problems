class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfdiv=[]
        for i in range(left, right+1):
            flag = 0
            for j in str(i):
                if int(j) == 0:
                    flag = 1
                    break
                if i%int(j) > 0: 
                    flag = 1
                    break
            if flag == 0:
                selfdiv.append(i)
                
        return selfdiv      
