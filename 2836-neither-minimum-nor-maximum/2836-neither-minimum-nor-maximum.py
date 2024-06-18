class Solution:
    def findNonMinOrMax(self, nums) -> int:
        if len(nums)<=2:
            return -1
        else:
            for i in nums:
                if i != min(nums) and i!= max(nums):
                    return i