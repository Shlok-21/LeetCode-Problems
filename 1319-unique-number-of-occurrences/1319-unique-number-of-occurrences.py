from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        return (len(Counter(arr).values()) == len(set(Counter(arr).values())))
        