class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        dp = {}
        def dfs(isAlice, i, M):
            if i >= len(piles): return 0
            if (isAlice, i, M) in dp: return dp[(isAlice, i, M)]
            sum_, res = 0, 0 if isAlice else float("inf")
            for j in range(1, (M * 2) + 1):
                if i + j > len(piles): break
                sum_ += piles[j + i - 1]
                if isAlice:
                    res = max(res, sum_ + dfs(False, j + i, max(M, j)))
                else:
                    res = min(res, dfs(True, j + i, max(M, j)))
            dp[(isAlice, i, M)] = res
            return res
        return dfs(True, 0, 1)