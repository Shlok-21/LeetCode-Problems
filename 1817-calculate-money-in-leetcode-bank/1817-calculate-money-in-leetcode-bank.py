class Solution:
    def totalMoney(self, n: int) -> int:
        sum = 0
        adder = 0
        while n>0:
            if n>=7:
                for i in range(1,8):
                    sum += i+adder             
                n-=7
                adder +=1
            else:
                for i in range(1,n+1):
                    sum+= i+adder
                n-=n
        return sum  