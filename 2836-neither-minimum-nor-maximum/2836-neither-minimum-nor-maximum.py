class Solution:
    def findNonMinOrMax(self, nums) -> int:
        if len(nums)<3:
            return -1
        else:
            return sorted(nums)[1]