class Solution:
    def minimumBuckets(self, A: str) -> int:
        @lru_cache(None)
        def dfs(i, monst, food):
            if i == len(A): 
                return inf if monst else 0
            if A[i] == '.':
                if monst:
                    return 1 + dfs(i+1, 0, 1)
                else:
                   return min(1+dfs(i+1, 0, 1), dfs(i+1, 0, 0))
            else:
                if food:
                    return dfs(i+1, 0, 0)
                elif not monst:
                    return dfs(i+1, 1, 0)
            return inf

        ans = dfs(0, 0, 0)
        return -1 if ans == inf else ans