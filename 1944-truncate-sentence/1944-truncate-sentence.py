class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ls = s.split(' ')
        st = [ls[x] for x in range(k)]
        return ' '.join(st)