class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj, res = defaultdict(set), 0
        for a, b in roads:
            adj[a].add(b)
            adj[b].add(a)
        for u in range(n):
            for v in range(u + 1, n):
                count = len(adj[u]) + len(adj[v])
                if u in adj[v] or v in adj[u]: count -= 1
                res = max(res, count)
        return res