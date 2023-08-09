class Solution:
    def minimizeMax(self, A: List[int], p: int) -> int:
        def check(mid):
            i, count = 1, 0
            while i < len(A):
                if A[i]-A[i-1] <= mid:
                    i += 1
                    count += 1
                i += 1
            return count >= p
        A.sort()
        l, r = 0, 10**9
        while r > l:
            mid = (r+l)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r