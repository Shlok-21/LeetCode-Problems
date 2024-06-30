class Solution:
    def findCenter(self, arr: List[List[int]]) -> int:
        if arr[0][0] in arr[1] and arr[0][0] in arr[2]:
            return arr[0][0]
        else:
            return arr[0][1]