class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        while nums:
            averages.append((max(nums) + min(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return min(averages)