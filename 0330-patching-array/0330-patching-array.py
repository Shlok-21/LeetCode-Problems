class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # nums=[1, 5, 10]    n= 20
        missing , patch , index = 1, 0, 0
        while missing <= n:
            if index < len(nums) and nums[index] <= missing:
                missing += nums[index]
                index +=1
            else:
                missing += missing
                patch +=1
        return patch