class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n, ptr, sum_ = len(arr), 0, 0
        dp = [float("inf")] * n
        for i, val in enumerate(arr):
            sum_ += val
            while sum_ > target:
                sum_ -= arr[ptr]
                ptr += 1
            if sum_ == target: 
                dp[i] = i - ptr + 1
        res, last = float("inf"), float("inf")
        for i, val in enumerate(dp):
            if i - val >= 0:
                res = min(res, dp[i - val] + val)
            last = min(val, last)
            dp[i] = last
        return -1 if res == float("inf") else res