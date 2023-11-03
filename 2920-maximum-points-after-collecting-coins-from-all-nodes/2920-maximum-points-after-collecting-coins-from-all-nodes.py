class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        A, visit, Q = defaultdict(list), set({0}), [0]
        
        while Q:
            node = Q.pop(0)
            for child in adj[node]:
                if child not in visit:
                    A[node].append(child)
                    visit.add(child)
                    Q.append(child)
                    
        @cache
        def dfs(node, inc):
            if inc == 15: return 0
            res = 0
            for child in A[node]:
                coin = coins[child]
                for _ in range(inc):
                    coin = floor(coin/2)
                
                res += max(dfs(child, inc) + (coin - k), dfs(child, inc + 1) + floor(coin / 2))
            return res
        
        return max(dfs(0, 0) + (coins[0] - k), dfs(0, 1) + floor(coins[0] / 2))