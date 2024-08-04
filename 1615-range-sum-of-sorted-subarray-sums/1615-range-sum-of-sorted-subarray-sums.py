class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        #print(nums, left, right)
        mod = 1000000007
        sub_arr = []
        for i in range(len(nums)):
            summ = nums[i]
            #print(summ)
            sub_arr.append(summ)
            for j in range(i+1, len(nums)):
                summ+=nums[j]
                sub_arr.append(summ)
        #print(f'sub_arr : {sub_arr}')
        sub_arr.sort()
        #print(sub_arr)
        return sum(sub_arr[left-1: right])%mod