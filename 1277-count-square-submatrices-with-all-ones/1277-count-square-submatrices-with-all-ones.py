class Solution:
    def countSquares(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dp = [[A[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] and i-1 >= 0 and j-1 >= 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return sum(sum(li) for li in dp)