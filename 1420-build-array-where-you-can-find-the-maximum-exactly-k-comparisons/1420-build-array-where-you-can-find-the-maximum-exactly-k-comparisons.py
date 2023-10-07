class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @lru_cache(None)
        def dfs(i, max_, count):
            if count > k: return 0
            if i == n: 
                return count == k
            res = 0
            for num in range(1, m+1):
                res += dfs(i+1, max(num, max_), count + int(num > max_))
            res %= 10**9+7
            return res
        return dfs(0, 0, 0)