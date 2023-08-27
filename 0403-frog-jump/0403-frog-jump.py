class Solution:
    def canCross(self, S: List[int]) -> bool:
        A = {num: i for i, num in enumerate(S)}
        @cache
        def dfs(i, last):
            if i == len(A)-1: return True
            res = False
            for k in [last-1, last, last+1]:
                if S[i]+k in A and i < A[k+S[i]]:
                    res = res or dfs(A[k+S[i]], k)
            return res
        return dfs(0, 0)