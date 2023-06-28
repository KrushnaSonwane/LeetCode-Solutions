class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        D, adj = {}, defaultdict(list)
        for i, (a, b) in enumerate(edges):
            adj[a].append([b, succProb[i]])
            adj[b].append([a, succProb[i]])
        Q = [[-1.0, start]]
        while Q:
            cost, node = heappop(Q)
            cost = -cost
            if node in D and D[node] >= cost: continue
            D[node] = cost
            if node == end: return cost
            for child, d in adj[node]:
                heappush(Q, [-float(cost*d), child])
        return 0