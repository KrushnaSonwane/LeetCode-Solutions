class Solution:
    def numberOfWays(self, startPos: int, endPos: int, A: int) -> int:
        mod = 10**9 + 7
        dp = {}
        def dfs(pos, k):
            if (pos, k) not in dp:
                if k == 0: return int(pos == endPos)
                # if pos < 0: return 0
                res = dfs(pos-1, k-1) + dfs(pos+1, k-1)
                dp[(pos, k)] = res
            return dp[(pos, k)]
        return dfs(startPos, A) % mod