from itertools import permutations
class Solution:
    def numTilePossibilities(self, s: str) -> int:
        sets = set()
        for i in range(1, len(s) +1):
            for val in permutations(s,i):
                sets.add(''.join(val))
        return len(sets)