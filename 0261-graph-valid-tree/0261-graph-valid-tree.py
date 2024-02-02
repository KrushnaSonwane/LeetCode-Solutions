class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit, Q = {0}, [(0, -1)]
        while Q:
            node, last = Q.pop(0)
            for child in adj[node]:
                if child == last: continue
                if child in visit: return False
                visit.add(child)
                Q.append([child, node])
        return len(visit) == n