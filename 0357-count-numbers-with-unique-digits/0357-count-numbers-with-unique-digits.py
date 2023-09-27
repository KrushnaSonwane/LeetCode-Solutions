class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        dp = {}
        def dfs(i, start, mask):
            if (i, start, mask) not in dp:
                if i == n: return start
                res = 0
                if not start:
                    res = dfs(i+1, start, mask)
                for d in range(1 if not start else 0, 10):
                    if mask[d] != '1':
                        A = [ch for ch in mask]
                        A[d] = '1'
                        res += dfs(i+1, 1, ''.join(A))
                dp[(i, start, mask)] = res
                return res
            return dp[(i, start, mask)]
            
        return dfs(0, False, '0' * 10) + 1