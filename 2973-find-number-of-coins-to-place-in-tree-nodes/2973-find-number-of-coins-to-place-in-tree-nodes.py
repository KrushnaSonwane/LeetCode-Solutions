class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, last):
            A = [cost[i]]
            for child in adj[i]:
                if last == child: continue
                A += dfs(child, i)
            A.sort(reverse = True)
            if len(A) < 3:
                res[i] = 1
                return A
            else:
                res[i] = max(A[0]*A[1]*A[2], A[0]*A[-1]*A[-2], 0)
            B, taken = [], 0
            while A and taken < 3:
                B.append(A.pop(0))
                taken += 1
            taken = 0
            while A and taken < 3:
                B.append(A.pop())
                taken += 1
            return B
        res = [0 for _ in range(len(cost))]
        dfs(0, -1)
        return res