class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit, res, adj = set(), 0, defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]: adj[i].append(j)
        def dfs(node):
            if node in visit: return
            visit.add(node)
            for child in adj[node]:
                dfs(child)
        for node in range(len(isConnected)):
            if node not in visit:
                res += 1
                dfs(node)
        return res