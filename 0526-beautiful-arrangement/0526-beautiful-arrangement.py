class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i, mask):
            if i == n+1: return 1
            res = 0
            for num in range(1, n+1):
                if mask[num] != '1' and 0 in [num%i, i%num]:
                    A = [ch for ch in mask]
                    A[num] = '1'
                    res += dfs(i+1, ''.join(A))
            return res
        return dfs(1, '0'*(n+1))