class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        def dfs(A):
            res = j = 0
            F, T = 0, 0
            for i, val in enumerate(A):
                if val == 'F': F += 1
                else: T += 1
                while F > k:
                    if A[j] == 'F': F -= 1
                    else:  T -= 1
                    j += 1
                res = max(res, F + T)
            return res
        ans = [a for a in A]
        for i, a in enumerate(ans):
            if a == 'T': ans[i] = 'F'
            else: ans[i] = 'T'
        return max(dfs(A), dfs(''.join(ans)))