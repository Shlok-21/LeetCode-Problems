class Solution:
    def triangularSum(self, nums):
        new = nums.copy()
        while len(new) >1:
            old = new.copy()
            new.clear()
            for i in range(len(old)-1):
                new.append((old[i] + old[i+1]) %10)
        else:
            return(new[0])
