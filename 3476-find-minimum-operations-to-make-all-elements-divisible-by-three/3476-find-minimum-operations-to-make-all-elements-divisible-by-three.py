class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i%3 == 0:
                continue
            elif i%2 == 0 and i%3 != 0:
                count +=1
            elif i%3 == 1 or i%3 == 2:
                count +=1
                
        return(count)