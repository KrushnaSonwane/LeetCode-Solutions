class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        pre, sum_ = [0], 0
        for dig in floor:
            sum_ += dig == '1'
            pre.append(sum_)
        dp = {}
        def dfs(i, k):
            if (i, k) not in dp:
                if len(floor) < i or k == 0: return 0
                curr = pre[min(len(floor), i + carpetLen - 1)] - pre[i - 1]
                res = max(dfs(i + 1, k), dfs(i + carpetLen, k - 1) + curr)
                dp[(i, k)] = res
            return dp[(i, k)]
        return pre[-1] - dfs(1, numCarpets)