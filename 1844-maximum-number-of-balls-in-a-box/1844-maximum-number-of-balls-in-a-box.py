class Solution:
    def countBalls(self, low: int, high: int) -> int:
        hashmap = defaultdict(int)

        for i in range(low, high+1):
            if i<10:
                hashmap[i] += 1
            else:
                summ=0
                for j in range(len(str(i))):
                    summ += (int(str(i)[j]))
                hashmap[summ] +=1

        return max(hashmap.values())