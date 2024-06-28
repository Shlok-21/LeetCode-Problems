class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        importance_vector = [0] * n
        for edge in roads:
            importance_vector[edge[0]] += 1
            importance_vector[edge[1]] += 1
        importance_vector = sorted(importance_vector, reverse = True)
        total = 0
        #start = 0
        for i in importance_vector:
            total += i*n
            n-=1
        return total