class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def check(mid):
            sum_ = 0
            if index >= mid - 1:
                sum_ += ((mid * (mid + 1)) // 2) + ((index - mid) + 1)
            else:
                temp = mid - index - 1
                sum_ += ((mid * (mid + 1)) // 2) - ((temp * (temp + 1)) // 2)
            if index + mid - 1 < n:
                sum_ += ((mid * (mid + 1)) // 2)
                temp = n - (index + mid)
                sum_ += temp
            else:
                temp = (n - index) + 1
                temp = (mid - temp) + 1
                sum_ += ((mid * (mid + 1)) // 2) - ((temp * (temp + 1)) // 2)
            sum_ -= mid
            return sum_ <= maxSum
        l, r = 1, maxSum
        res = 0
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res