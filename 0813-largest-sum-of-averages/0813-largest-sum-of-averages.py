class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        dp = {}
        for i in range(1, len(A)): A[i] += A[i - 1]
        def dfs(i, k):
            if (i, k) not in dp:
                if i == len(A): return 0
                if k == 1:
                    sum_ = A[-1] if i == 0 else A[-1] - A[i - 1]
                    size = len(A) - i
                    return sum_ / size
                res = 0
                for j in range(i, len(A) - (k - 1)):
                    sum_, size = A[j] if i == 0 else A[j] - A[i - 1], (j - i + 1)
                    res = max(res, sum_ / size + dfs(j + 1, k - 1))
                dp[(i, k)] = res
            return dp[(i, k)]
        return dfs(0, k)