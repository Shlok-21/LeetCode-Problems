class Solution:
    def findCenter(self, arr: List[List[int]]) -> int:
        main = arr[0][0]
        if main == arr[1][0] or  main == arr[1][1]:
            return main
        return arr[0][1]