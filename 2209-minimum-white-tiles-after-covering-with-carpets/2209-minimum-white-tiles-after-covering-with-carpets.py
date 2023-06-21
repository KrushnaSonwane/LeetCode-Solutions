class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        pre, sum_ = [0], 0
        for dig in floor:
            sum_ += dig == '1'
            pre.append(sum_)
        @cache
        def dfs(i, k):
            if len(floor) < i or k == 0: return 0
            res = dfs(i + 1, k)
            curr = pre[min(len(floor), i + carpetLen - 1)] - pre[i - 1]
            res = max(res, dfs(i + carpetLen, k - 1) + curr)
            return res
        return pre[-1] - dfs(1, numCarpets)