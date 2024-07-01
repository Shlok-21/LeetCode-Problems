class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        summ = 0
        for i in arr:
            if i%2 == 1:
                summ += 1
            else:
                summ = 0
            if summ == 3:
                return True
        return False