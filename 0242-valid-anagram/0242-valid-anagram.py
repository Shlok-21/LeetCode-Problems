class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = defaultdict(int)
        hash2 = defaultdict(int)

        for a in s:
            hash1[a] += 1
        for a in t:
            hash2[a] += 1

        return hash1 == hash2