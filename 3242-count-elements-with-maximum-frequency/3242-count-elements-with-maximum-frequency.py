class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        summ = 0
        counts = {x: nums.count(x) for x in nums}   
        
        for i in (counts.values()):
            if i == max(counts.values()):
                summ += i
        return summ