class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i, val in enumerate(manager): adj[val].append(i)
        def dfs(node):
            if not adj[node]: return 0
            return max(informTime[node] + dfs(child) for child in adj[node])
        return dfs(headID)