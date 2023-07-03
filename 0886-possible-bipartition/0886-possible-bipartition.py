class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        color = defaultdict(str)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, C):
            color[node] = C
            res = True
            for child in adj[node]:
                if child not in color:
                    res = res and dfs(child, 'g' if C == 'r' else 'r')
                else:
                    if color[child] == C: return False
            return res
        
        for node in range(n):
            if node not in color:
                if not dfs(node, 'r'): return False
        return True