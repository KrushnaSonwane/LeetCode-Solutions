class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(A, k, num):
            if k==0:
                res.append(A.copy())
                return
            for i in range(num, n+1):
                A.append(i)
                dfs(A, k-1, i+1)
                A.pop()
        res = []
        dfs([], k, 1)
        return res