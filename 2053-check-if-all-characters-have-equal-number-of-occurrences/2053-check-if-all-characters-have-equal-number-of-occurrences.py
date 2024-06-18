class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {x : s.count(x) for x in s}
        print(counts)
        
        if len({x for _,x in counts.items()}) == 1:
            return True
        else:
            return False
            