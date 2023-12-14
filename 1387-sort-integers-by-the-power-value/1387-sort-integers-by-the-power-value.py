class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @cache
        def dfs(num):
            if num == 1: return 0
            return 1 + (dfs(num*3+1) if num % 2 else dfs(num//2))
        return sorted([[dfs(i), i] for i in range(lo, hi+1)])[k-1][1]