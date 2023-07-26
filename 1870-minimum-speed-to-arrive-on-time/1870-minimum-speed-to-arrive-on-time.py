class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        res, l, r = inf, 1, 10**9
        def check(mid):
            sum_ = 0
            for i in range(len(dist)-1):
                sum_ += ceil(dist[i]/mid)
            return sum_ + dist[-1]/mid <= hour
        while r >= l:
            mid = (r+l)//2
            if check(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res if res != inf else -1