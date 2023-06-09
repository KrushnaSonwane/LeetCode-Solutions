class Solution:
    def numberOfWays(self, startPos: int, endPos: int, A: int) -> int:
        mod = 10**9 + 7
        dp = {}
        def dfs(pos, k):
            if (pos, k) not in dp:
                if k == 0: return int(pos == endPos)
                dp[(pos, k)] = (dfs(pos-1, k-1) + dfs(pos+1, k-1)) % mod
            return dp[(pos, k)]
        return dfs(startPos, A) 