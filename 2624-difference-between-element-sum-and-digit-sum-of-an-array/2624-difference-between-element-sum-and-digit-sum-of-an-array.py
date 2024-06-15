class Solution:
    def differenceOfSum(self, nums):
        summ = sum(nums)
        summ2 = 0
        for i in nums:
            for j in str(i):
                summ2 += int(j)
        return abs(summ-summ2)