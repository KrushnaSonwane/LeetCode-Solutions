class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        inDegree, adj = [0 for _ in range(n)], defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            inDegree[a] += 1
            inDegree[b] += 1
        Q, res = [], []
        for i in range(n):
            if inDegree[i] == 1:
                Q.append(i)
                inDegree[i] -= 1
        while Q:
            res = Q.copy()
            for _ in range(len(Q)):
                node = Q.pop(0)
                for child in adj[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        Q.append(child)
        return res