class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        A = [[a, b] for a, b in zip(ages, scores)]
        A.sort(key = lambda x: (x[0], x[1]))
        @cache
        def dfs(i, j):
            if j == len(A): return 0
            res = dfs(i, j + 1)
            if i == -1 or A[i][0] == A[j][0] or (A[i][0] < A[j][0] and A[i][1] <= A[j][1]):
                res = max(res, A[j][1] + dfs(j, j + 1))
            return res
        return dfs(-1, 0)