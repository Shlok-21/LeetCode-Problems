class Solution:
    def minPairSum(self, nums) -> int:
        nums.sort()
        max_sum = 0
        n = len(nums)
        for i in range(n//2):
            summ = nums[i] + nums[n-1 - i]
            max_sum = max(max_sum, summ)
        return max_sum