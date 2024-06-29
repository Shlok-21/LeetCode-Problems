class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [[] for _ in range(n)]
        ans = []
        
        index_dict = defaultdict(list)
        for u, v in edges:
            index_dict[v].append(u)
        
        def dfs(node, visited, acc):
            if node in visited:
                return
            visited.add(node)
            for ancestor in index_dict[node]:
                acc.add(ancestor)
                dfs(ancestor, visited, acc)
        
        for node in range(n):
            visited = set()
            acc = set()
            dfs(node, visited, acc)
            ancestors[node] = sorted(list(acc))
        
        return ancestors