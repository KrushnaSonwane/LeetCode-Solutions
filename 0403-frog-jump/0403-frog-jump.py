class Solution:
    def canCross(self, stones: List[int]) -> bool:
        hashT = {val: i for i, val in enumerate(stones)}
        @cache
        def dfs(i, last):
            if i >= len(stones) - 1: return True
            res = False
            for jump in [last - 1, last, last + 1]:
                curr = stones[i] + jump
                if curr in hashT and hashT[curr] > i:
                    res = res or dfs(hashT[curr], jump)
            return res
        return dfs(0, 0)