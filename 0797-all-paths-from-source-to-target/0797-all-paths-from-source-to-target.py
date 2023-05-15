class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, n = [], len(graph)
        adj = defaultdict(list)
        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)
        def dfs(node, li):
            if node == n - 1:
                res.append(li)
            for child in adj[node]:
                li.append(child)
                dfs(child, li.copy())
                li.pop()
        dfs(0, [0])
        return res