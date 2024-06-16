from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = Counter(s)
        t1 = Counter(t)
        sum=0
        s1.subtract(t1)
        for i in s1:
            if s1.get(i) > 0:
                print(s1.get(i))
                sum+=int(s1.get(i))
        return sum