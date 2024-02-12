class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        A = Counter(nums)
        A = [[num, A[num]] for num in A]
        A.sort()
        print(A)
        @cache
        def dfs(i):
            if i >= len(A): return 0
            res = dfs(i+1)
            j = i + 1
            if j < len(A):
                if A[j][0] == A[i][0] + 1:
                    j += 1
            res = max(res, dfs(j) + A[i][0] * A[i][1])
            return res
        return dfs(0)
            