class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        countt = 1 if a == b else 0
        for i in range(1,int(max(a,b)/2)+1):
            if a%i == 0 and b%i == 0:
                countt +=1

        return countt