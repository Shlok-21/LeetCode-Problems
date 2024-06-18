class Solution:
    def sumOfUnique(self, nums) -> int:
        counts = {x : nums.count(x) for x in nums}
        vals = [key for key, values in counts.items() if values ==1]
        return sum(vals)