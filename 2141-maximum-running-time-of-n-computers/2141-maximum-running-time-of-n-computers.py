class Solution:
    def maxRunTime(self, n: int, B: List[int]) -> int:
        B.sort()
        def check(mid):
            sum_, count = 0, 0
            for num in B:
                sum_ += num
                if sum_ >= mid:
                    sum_ -= mid
                    count += 1
            return count >= n
        l, r = 1, sum(B)+1
        while r > l:
            mid = (r+l)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l-1