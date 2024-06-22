class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        ans = 0
        count = 0
        for j in nums:
            if j & 1:
                k -= 1
                count = 0
                print('found odd')
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            ans += count

        return ans