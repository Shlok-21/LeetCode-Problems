class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1,n+1)]
        current_pos = 0
        eliminate = 1
        while len(arr) > 1:
            if eliminate == k:
                arr.pop(current_pos)
                current_pos -= 1
                eliminate = 0
            else:
                current_pos += 1
                eliminate += 1
            if current_pos >= len(arr):
                current_pos = 0
            if eliminate >k:
                eliminate = 1
        
        return arr[0]