class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge = edges[0][0]
        if edge == edges[1][0] or edges[1][1] == edge:
            return edge
        return edges[0][1]