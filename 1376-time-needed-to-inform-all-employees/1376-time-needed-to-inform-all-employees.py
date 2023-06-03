class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i, val in enumerate(manager):
            adj[val].append(i)
        res = [0]
        def dfs(node):
            if not adj[node]:
                return 0
            res = 0
            for child in adj[node]:
                res = max(res, dfs(child) + informTime[node])
            return res
        return dfs(headID)