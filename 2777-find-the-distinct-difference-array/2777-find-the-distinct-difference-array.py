class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i <= len(nums)-1:
            ans.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
            i+=1
            print(ans)
        return ans