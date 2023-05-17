import bisect
class Solution(object):
    def fullBloomFlowers(self, F, P):
        start = sorted(a for a, _ in F)
        end = sorted(b for _, b in F)
        n, res = len(F), []
        for key in P:
            l = bisect.bisect_right(start, key)
            r = bisect.bisect_left(end, key)
            res.append(l - r)
        return res