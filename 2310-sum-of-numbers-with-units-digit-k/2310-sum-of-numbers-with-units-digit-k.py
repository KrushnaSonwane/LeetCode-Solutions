class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        A = [k]
        while A[-1]+10 <= num:
            A.append(A[-1]+10)
        if A[0]==0: A.pop(0)
        @cache
        def dfs(i, sum_):
            if sum_ == 0: return 0
            if i >= len(A): return inf
            if A[i] > sum_: return inf
            return min(dfs(i+1, sum_), 1 + dfs(i, sum_ - A[i]))
        return dfs(0, num) if dfs(0, num) != inf else -1