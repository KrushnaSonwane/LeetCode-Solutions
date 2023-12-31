class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i, j, alice):
            if i >= j:
                return 0
            if alice:
                res = max(dfs(i+1, j, 0) + piles[i], dfs(i, j-1, 0) + piles[j])
            else:
                res = min(dfs(i+1, j, 0) + piles[i], dfs(i, j-1, 0) + piles[j])
            return res
        res = dfs(0, len(piles)-1, 1)
        return 0 if res < 0 else 1