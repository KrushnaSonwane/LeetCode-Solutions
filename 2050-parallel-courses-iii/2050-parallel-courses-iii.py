class Solution:
    def minimumTime(self, n: int, graph: List[List[int]], time: List[int]) -> int:
        adj, inDegree = defaultdict(list), [0]*n
        for a, b in graph:
            adj[a].append(b)
            inDegree[b-1] += 1
        Q, res = [], [-inf] * n
        for i, d in enumerate(inDegree):
            if d == 0:
                Q.append(i+1)
                res[i] = time[i]
        while Q:
            node = Q.pop(0)
            for child in adj[node]:
                inDegree[child-1] -= 1
                res[child-1] = max(res[node-1]+time[child-1], res[child-1])
                if inDegree[child-1] == 0:
                    Q.append(child)
        return max(res)