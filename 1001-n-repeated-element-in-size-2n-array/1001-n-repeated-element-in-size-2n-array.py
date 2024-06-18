from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums) -> int:
        hmap = defaultdict(int)

        for i in nums:
            hmap[i] = hmap[i]+1
            
        for k,v in hmap.items():
            if v != 1:
                return k