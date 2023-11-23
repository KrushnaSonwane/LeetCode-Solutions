class Solution:
    def minWastedSpace(self, P: List[int], B: List[List[int]]) -> int:
        res, MOD = inf, 10**9+7
        P.sort()
        for A in B:
            A.sort()
            if A[-1] < P[-1]: continue
            i, sum_ = 0, 0
            for key in A:
                l, r = 0, len(P)-1
                ans = i-1
                while r >= l:
                    mid = (r + l) // 2
                    if P[mid] > key:
                        r = mid - 1
                    else:
                        ans = mid
                        l = mid + 1
                sum_ += (ans-i+1) * key
                i = ans+1
            res = min(res, sum_)
        if res == inf: return -1
        return (res - sum(P)) %  MOD