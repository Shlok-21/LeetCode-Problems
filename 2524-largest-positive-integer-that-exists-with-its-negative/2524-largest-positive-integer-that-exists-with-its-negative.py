class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        for i in sorted(nums):
            if -(i) in nums:
                return abs(i)
        return -1
