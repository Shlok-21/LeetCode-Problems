class Solution:
    def findGCD(self, nums):
        gcd = 0
        minn, maxx = min(nums), max(nums)
        for i in range(1,minn+1):
            print(i, minn, maxx)
            if (minn % i==0) and (maxx % i == 0):
                gcd = i
        return gcd