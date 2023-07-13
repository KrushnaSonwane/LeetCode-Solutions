class Solution:
    def canFinish(self, N: int, A: List[List[int]]) -> bool:
        adj = defaultdict(list)
        degree = [0]*N
        for a, b in A:
            adj[a].append(b)
            adj[b].append(a)
            degree[a] += 1
        Q, visit = [], set()
        for i in range(N):
            if not degree[i]:
                Q.append(i)
                visit.add(i)
        while Q:
            node = Q.pop(0)
            for child in adj[node]:
                degree[child] -= 1
                if child not in visit:
                    if not degree[child]: 
                        Q.append(child)
                        visit.add(child)
        return len(visit) == N