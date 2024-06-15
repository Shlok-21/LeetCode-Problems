class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        if len(piles) == 3:
            return piles[1]
        else:
            maxx =  piles[int(len(piles)/3):]
        return sum([maxx[i] for i in range(0,len(maxx),2)])