class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def dfs(num):
            if num == 1: return 0
            if num%2:
                return 1 + dfs(num*3+1)
            return 1 + dfs(num // 2)
        A = sorted([[dfs(i), i] for i in range(lo, hi+1)])
        return A[k-1][1]