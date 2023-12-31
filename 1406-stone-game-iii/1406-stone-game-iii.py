class Solution:
    def stoneGameIII(self, A: List[int]) -> str:
        @cache
        def dfs(i, alice):
            if i == len(A):
                return 0
            if alice:
                res = dfs(i+1, 0) + A[i]
                if i + 1 < len(A):
                    res = max(res, dfs(i+2, 0) + A[i]+A[i+1])
                if i + 2 < len(A):
                    res = max(res, dfs(i+3, 0) + A[i]+A[i+1]+A[i+2])
            else:
                res = dfs(i+1, 1) - A[i]
                if i + 1 < len(A):
                    res = min(res, dfs(i+2, 1) - (A[i]+A[i+1]))
                if i + 2 < len(A):
                    res = min(res, dfs(i+3, 1) - (A[i]+A[i+1]+A[i+2]))
            return res
        res = dfs(0, 1)
        if res > 0:
            return 'Alice'
        elif res < 0:
            return 'Bob'
        return 'Tie'