class Solution:
    def new21Game(self, N, K, maxPts):
        if K == 0: return 1.0
        if N >= K - 1 + maxPts: return 1.0
        dp = [0.0] * (N + 1)
        res, sum_, dp[0] = 0.0, 1.0, 1.0
        for i in range(1, N + 1):
            dp[i] = sum_ / maxPts
            if i < K:
                sum_ += dp[i]
            else:
                res += dp[i]
            if i >= maxPts:
                sum_ -= dp[i - maxPts]
        return res