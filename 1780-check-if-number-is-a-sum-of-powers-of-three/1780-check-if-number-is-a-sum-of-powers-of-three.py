class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        num, A = 0, []
        while 3 ** num <= n:
            A.append(3**num)
            num += 1
        @cache
        def dfs(i, sum_):
            if sum_ == 0: return True
            if i == len(A): return False
            res = dfs(i+1, sum_)
            if A[i] <= sum_:
                res = res or dfs(i+1, sum_-A[i])
            return res
        return dfs(0, n)