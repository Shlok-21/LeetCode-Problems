class Solution:
    def minOperations(self, n: int) -> int:
        arr = [ (2*x)+1 for x in range(n)]
        mean = int(sum(arr)/len(arr))
        steps = 0
        for i in range(int(mean/2)):
            steps += (mean- arr[i])
            
        return steps