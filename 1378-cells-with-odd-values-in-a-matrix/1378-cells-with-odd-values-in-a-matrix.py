class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        initial = []
        for _ in range(m):
            initial.append([0]*n)
        
        for row in indices:
            for j in range(len(initial[row[0]])):
                initial[row[0]][j]+=1
            
        rows = []
        for i in indices:
            rows.append(i[1])
        
        for col in rows:
            for i in range(len(initial)):
                (initial[i][col])+=1
        
        count = 0
        for i in initial:
            for j in i:
                if j%2 == 1:
                    count +=1
        return count
            