class Solution:
    def minIncrementForUnique(self, nums) -> int:
        nums.sort()
        steps = 0
        tracker = 0        
        
        for num in nums:
            tracker = max(tracker , num)
            steps += tracker - num
            tracker+=1
        return steps