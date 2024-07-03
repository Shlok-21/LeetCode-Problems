class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0
        nums.sort()
        left = 0
        right = len(nums) - 3
        ans = []
        for i in range(4):
            nums_checker = nums[left:right]
            curr_diff = max(nums_checker) - min(nums_checker)
            if not ans:
                ans.append(curr_diff)
            elif ans[0] > curr_diff:
                ans[0] = curr_diff
            left+=1
            right +=1
        return int(ans[0])