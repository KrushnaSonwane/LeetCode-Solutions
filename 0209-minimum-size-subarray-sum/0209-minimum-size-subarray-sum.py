class Solution:
    def minSubArrayLen(self, T: int, A: List[int]) -> int:
        res, j = inf, 0
        sum_ = 0
        for i, num in enumerate(A):
            sum_ += num
            while sum_ >= T:
                res = min(res, i - j + 1)
                sum_ -= A[j]
                j += 1
        return 0 if res == inf else res