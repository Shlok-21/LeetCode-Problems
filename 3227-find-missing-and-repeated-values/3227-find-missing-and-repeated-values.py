class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        total = len(grid)*len(grid)
        elements = {x for x in range(1,total+1)}
        remainder = []

        for i in grid:
            for j in i:
                if j in elements:
                    elements.remove(j)
                else:
                    remainder.append(j)
        return([remainder[0], list(elements)[0]]) 