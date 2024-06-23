class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:].zfill(32)  
        y = bin(y)[2:].zfill(32)  

        summ = 0
        for i, j in zip(x,y):
            if i != j:
                summ +=1
        return int(summ)