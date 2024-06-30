class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            flag = True
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()
            diff = sub_arr[1] - sub_arr[0]
            for i in range(len(sub_arr)-1):
                if (sub_arr[i+1] - sub_arr[i]) != diff:
                    flag = False
                    break 
            ans.append(flag)
        return ans  