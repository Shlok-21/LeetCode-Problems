class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        summ =0
        for i in nums:
            if len(str(i))%2 ==0:
                summ +=1
        return summ