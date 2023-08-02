class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(A):
                res.append(A.copy())
                return
            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]
                dfs(i+1)
                A[i], A[j] = A[j], A[i]
        res = []
        dfs(0)
        return res