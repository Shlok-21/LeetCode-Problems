class Solution:
    def findCenter(self, arr: List[List[int]]) -> int:
        for i in arr[0]:
            if i in arr[1]:
                return i