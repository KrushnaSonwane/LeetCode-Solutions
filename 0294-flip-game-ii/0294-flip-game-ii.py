class Solution:
    def canWin(self, s: str) -> bool:
        @cache
        def dfs(A, you):
            res = not you
            if you:
                B = [ch for ch in A]
                for i in range(1, len(A)):
                    if A[i-1] == A[i] == '+':
                        B[i-1] = B[i] = '-'
                        res = res or dfs(''.join(B), False)
                        B[i-1] = B[i] = '+'
            else:
                B = [ch for ch in A]
                for i in range(1, len(A)):
                    if A[i-1] == A[i] == '+':
                        B[i-1] = B[i] = '-'
                        res = res and dfs(''.join(B), True)
                        B[i-1] = B[i] = '+'
            return res
        return dfs(s, True)