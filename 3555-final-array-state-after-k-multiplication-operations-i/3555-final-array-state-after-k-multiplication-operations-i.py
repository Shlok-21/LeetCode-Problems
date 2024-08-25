class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minn = min(nums)
            index_minn = nums.index(minn)
            nums[index_minn] *= multiplier
        return nums