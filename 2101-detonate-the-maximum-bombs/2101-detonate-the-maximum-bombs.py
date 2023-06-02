class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        res, adj = 0, defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)
        def dfs(node):
            if node in visit: return 0
            visit.add(node)
            count = 0
            for child in adj[node]:
                if child not in visit:
                    count += dfs(child) + 1
            return count
        for i in range(n):
            visit = set()
            res = max(res, dfs(i) + 1)
        return res