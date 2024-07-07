class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minn = min(nums) +k
        maxx = max(nums) -k
        diff = maxx - minn
        return max(0, diff)