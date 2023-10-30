class Solution:
    def knightDialer(self, n: int) -> int:
        MOD, dp = 10**9+7, {}
        hashT = {'0': '46', '1': '68', '2': '79', '3': '48', '4': '039', '5': '' ,'6': '017', '7': '26', '8': '13', '9': '24', ' ': '0123456789'}
        def dfs(i, x):
            if (i, x) not in dp:
                if i == n: return 1
                res = 0
                for num in hashT[x]:
                    res += dfs(i+1, num)
                dp[(i, x)] = res % MOD
            return dp[(i, x)]
        return dfs(0, ' ')