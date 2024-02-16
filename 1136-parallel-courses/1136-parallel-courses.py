class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, degree = defaultdict(list), [0 for _ in range(n+1)]
        for a, b in relations:
            degree[b] += 1
            adj[a].append(b)
        Q = []
        for i in range(n+1):
            if i != 0 and degree[i] == 0:
                Q.append(i)
        if not Q: return -1
        res = 0
        while Q:
            for _ in range(len(Q)):
                node = Q.pop(0)
                for child in adj[node]:
                    degree[child] -= 1
                    if degree[child] == 0:
                        Q.append(child)
            res += 1
        return res if sum(degree) == 0 else -1