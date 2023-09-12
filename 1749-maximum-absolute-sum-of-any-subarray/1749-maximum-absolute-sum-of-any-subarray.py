class Solution:
    def maxAbsoluteSum(self, A: List[int]) -> int:
        
        @lru_cache(None)
        def dfs1(i, s, e):
            if i == len(A):
                return 0 if s else -inf
            if e: return 0
            if s:
                res = max(0, A[i] + dfs1(i+1,s,e))
            else:
                res = max(dfs1(i+1,s,e), A[i]+dfs1(i+1,1,e))
            return res

        @lru_cache(None)
        def dfs2(i, s, e):
            if i == len(A):
                return 0 if s else inf
            if e: return 0
            if s:
                res = min(0, A[i] + dfs2(i+1,s,e))
            else:
                res = min(dfs2(i+1,s,e), A[i]+dfs2(i+1,1,e))
            return res
            
        return max(dfs1(0,0,0), abs(dfs2(0,0,0)))