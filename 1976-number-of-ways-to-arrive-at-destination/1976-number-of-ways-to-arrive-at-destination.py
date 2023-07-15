class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, w in roads:
            adj[a].append([b, w])
            adj[b].append([a, w])
        dist = [inf] * n
        res, mod = defaultdict(int), 10**9+7
        res[0], Q = 1, [[0,0]]
        while Q:
            cost, node = heappop(Q)
            for child, w in adj[node]:
                if cost + w < dist[child]:
                    dist[child] = cost + w
                    heappush(Q, [cost+w, child])
                    res[child] = res[node]
                elif cost + w == dist[child]:
                    res[child] += res[node]
        return res[n-1] % mod