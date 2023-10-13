class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append([b, d])
            adj[b].append([a, d])
        res, visit, Q = inf, set({1}), [1]
        while Q:
            node = Q.pop(0)
            for child, d in adj[node]:
                res = min(d, res)
                if child not in visit:
                    visit.add(child)
                    Q.append(child)
        return res