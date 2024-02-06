class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit, Q, res = set(), [], 0
        for node in range(n):
            if node not in visit:
                res += 1
                Q = [node]
                while Q:
                    node = Q.pop(0)
                    for child in adj[node]:
                        if child not in visit:
                            visit.add(child)
                            Q.append(child)
        return res