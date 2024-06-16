class Solution:
    def largestAltitude(self, gain) -> int:
        alts = [0]
        for i in range(1,len(gain)+1):
            alts.append(alts[i-1] + gain[i-1])
        return max(alts)