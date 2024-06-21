from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ans = 0
        summ = sum(arr[:k]) 

        for i in range(k, n):
            if summ/k >= threshold:
                ans +=1
            summ += arr[i] - arr[i-k] 

        if summ/k >= threshold:
            ans +=1
        return ans