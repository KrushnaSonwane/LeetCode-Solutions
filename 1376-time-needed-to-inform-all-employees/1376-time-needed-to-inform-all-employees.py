class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i, val in enumerate(manager):
            adj[val].append(i)
        res = [0]
        def dfs(node, time):
            if not adj[node]:
                res[0] = max(res[0], time)
            for child in adj[node]:
                dfs(child, time + informTime[node])
        dfs(headID, 0)
        return res[0]