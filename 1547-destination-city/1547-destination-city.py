class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        end = []

        for path in paths:
            start.append(path[0])
            end.append(path[1])
        
        for i in end:
            if i not in start: return i