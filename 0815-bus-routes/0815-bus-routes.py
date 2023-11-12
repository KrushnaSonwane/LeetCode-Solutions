class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        A = defaultdict(list)
        for i, li in enumerate(routes):
            for a in li:
                A[a].append(i)
        dist, Q = {}, []
        if source == target and source in A: return 0
        for i in A[source]:
            dist[i] = 1
            heappush(Q, (1, i))
        while Q:
            cost, i = heappop(Q)
            for child in routes[i]:
                if child == target: return cost
                for j in A[child]:
                    if j in dist and dist[j] <= cost + 1: continue
                    dist[j] = cost + 1
                    heappush(Q, (cost+1, j))
        return -1