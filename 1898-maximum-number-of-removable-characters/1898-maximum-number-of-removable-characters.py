class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        hashT = {val: i for i, val in enumerate(removable)}
        l, r = 0, len(removable) - 1
        def isValid(mid):
            ptr1, ptr2 = 0, 0
            m, n = len(s), len(p)
            while ptr1 < m and ptr2 < n:
                if ptr1 not in hashT or hashT[ptr1] > mid:
                    if p[ptr2] == s[ptr1]:
                        ptr2 += 1
                ptr1 += 1
            return ptr2 == n
        res = 0
        while r >= l:
            mid = (r + l) // 2
            if isValid(mid):
                l = mid + 1
                res = max(res, mid + 1)
            else:
                r = mid - 1
        return res