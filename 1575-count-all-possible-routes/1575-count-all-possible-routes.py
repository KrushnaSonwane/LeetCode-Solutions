class Solution:
    def countRoutes(self, A: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i, fuel):
            res = 0
            if i == finish: res += 1
            for j in range(len(A)):
                if i != j and fuel >= abs(A[i] - A[j]):
                    res += dfs(j, fuel - abs(A[i] - A[j])) 
            return res % MOD
        return dfs(start, fuel)