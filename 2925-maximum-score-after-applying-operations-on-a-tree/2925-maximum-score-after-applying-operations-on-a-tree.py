class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        adj = defaultdict(list)
        A = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        Q = [0]
        visit = {0}
        while Q:
            node = Q.pop(0)
            for child in adj[node]:
                if child not in visit:
                    visit.add(child)
                    Q.append(child)
                    A[node].append(child)
        print(A)
        @cache
        def dfs(node, taken):
            if not A[node]:
                if not taken: return -inf
                return 0
            res = 0
            for child in A[node]:
                if taken:
                    res += dfs(child, taken) + values[child]
                else:
                    res += max(dfs(child, True), dfs(child, taken) + values[child], 0)
            # print(res, node, taken)
            return res
                    
        
        return max(dfs(0, False) + values[0], dfs(0, True))