class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for i in nums:
            for j in range(len(str(i))):
                arr.append(int(str(i)[j]))
        return(arr)