class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        A, n = [0], len(nums)
        for num in nums:
            A.append(A[-1]+num)
        dp = {i : [0, inf] for i in range(n+1)}
        dp[0] = [0, 0]
        for i in range(1, n+1):
            key = dp[i-1][1] + A[i-1]
            j = bisect_right(A, key-1)
            if j < len(A):
                if dp[j][0] < dp[i-1][0]+1:
                    dp[j][0] = dp[i-1][0]+1
                    dp[j][1] = A[j] - A[i-1]
                elif dp[j][0] == dp[i-1][0]+1:
                    dp[j][1] = min(dp[j][1], A[j]-A[i-1])
                    
            if dp[i-1][0] > dp[i][0]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1] + A[i]-A[i-1]
            elif dp[i-1][0] == dp[i][0]:
                dp[i][1] = min(dp[i][1], A[i]-A[i-1]+dp[i-1][1])

        return max(dp[i][0] for i in dp)