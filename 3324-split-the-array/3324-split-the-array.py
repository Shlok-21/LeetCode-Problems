class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        hash = {x : nums.count(x) for x in nums}
        print(hash.values())
        for i in hash.values():
            print(i)
            if i > 2:
                return False
        return True