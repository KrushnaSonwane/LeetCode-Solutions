class Solution:
    def maxLength(self, A: List[str]) -> int:
        @cache
        def dfs(i, chars):
            if len(chars) > 26: return 0
            if i == len(A):
                if len(chars) == len(set(chars)): return len(chars)
                return 0
            res = dfs(i+1, chars)
            for ch in A[i]:
                chars += ch
            res = max(res, dfs(i+1, chars))
            return res
        return dfs(0, '')