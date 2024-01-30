class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adj, res = defaultdict(list), [1]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(i, last):
            curr, count = colors[i], 1
            for child in adj[i]:
                if child != last:
                    a, b = dfs(child, i)
                    if a == curr:
                        count += b
                    else:
                        count, curr = -inf, inf
            res[0] = max(res[0], count)
            return curr, count
        dfs(0, -1)
        return res[0]
