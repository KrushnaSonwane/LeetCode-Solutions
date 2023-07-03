class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in paths:
            adj[a].append(b)
            adj[b].append(a)
        res = used = [-1]*n
        for node in range(1, n+1):
            for ty in [1,2,3,4]:
                for child in adj[node]:
                    if used[child-1] == ty: break
                else: 
                    res[node-1] = ty
                    used[node-1] = ty
        return res