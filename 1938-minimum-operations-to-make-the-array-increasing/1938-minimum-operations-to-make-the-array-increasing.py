class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps=0
        for i in range(len(nums)-1):
            print(f'i is {i}')
            while nums[i] >= nums[i+1]:
                adder = abs(nums[i+1] - nums[i]) +1
                nums[i+1] += adder
                steps += adder
                adder = 0
        return steps