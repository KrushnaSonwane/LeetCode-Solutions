class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def check(k):
            A = Counter()
            for i in range(k, len(s)+1):
                ss = s[i-k: i]
                A[ss] += 1
                if A[ss] == 2: return True
            return False
        l, r = 1, len(s)-1
        res = 0
        while r >= l:
            mid = (r + l) // 2
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res