class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        adj = defaultdict(list)
        for u, v, c in times:
            adj[u].append([v, c])
        visit, dist = set({k}), [float("inf")] * (n + 1)
        queue = [[0, k]]
        heapq.heapify(queue)
        while queue:
            cost, node = heapq.heappop(queue)
            visit.add(node)
            if len(visit) == n: return cost
            if dist[node] > cost:
                dist[node] = cost
                for child, c in adj[node]:
                    heapq.heappush(queue, [cost + c, child])
        return -1