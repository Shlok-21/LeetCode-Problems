class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        arr = []
        hash = Counter((groupSizes))
        for i in range(min(groupSizes), max(groupSizes)+1):
            if hash.get(i):
                while hash.get(i) > 0:
                    sub =[]
                    for j in range(i):
                        sub.append(groupSizes.index(i))
                        hash[i] -= 1
                        groupSizes[groupSizes.index(i)] = 0
                    arr.append(sub)
        return arr