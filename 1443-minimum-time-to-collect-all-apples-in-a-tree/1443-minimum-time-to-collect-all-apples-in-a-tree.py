class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visit = {0}
        def dfs(node):
            has = hasApple[node]
            res = 0
            for child in adj[node]:
                if child not in visit:
                    visit.add(child)
                    y, x = dfs(child)
                    if x: res += y + 2
                    has = has or x
            return res, has
        res, has = dfs(0)
        return res