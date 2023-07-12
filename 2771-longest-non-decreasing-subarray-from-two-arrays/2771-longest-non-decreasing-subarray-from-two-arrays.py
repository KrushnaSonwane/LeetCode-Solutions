class Solution:
    def maxNonDecreasingLength(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = dp[0][1] = 1
        for i in range(1, n):
            if A[i] >= A[i-1] and A[i] >= B[i-1]:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]) + 1
            elif A[i] >= A[i-1]:
                dp[i][0] = dp[i-1][0] + 1
            elif A[i] >= B[i-1]:
                dp[i][0] = dp[i-1][1] + 1
            else:
                dp[i][0] = 1
            
            if B[i] >= A[i-1] and B[i] >= B[i-1]:
                dp[i][1] = max(dp[i-1][0], dp[i-1][1]) + 1
            elif B[i] >= A[i-1]:
                dp[i][1] = dp[i-1][0] + 1
            elif B[i] >= B[i-1]:
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][1] = 1
        return max(max(a, b) for a, b in dp)