class Solution:
    def rotatedDigits(self, n: int) -> int:
        def dfs(s):
            for d in ['3', '4', '7']:
                if d in s: return 0
            for d in ['2', '5', '6', '9']:
                if d in s: return 1
            return 0
        res = 0
        for num in range(1, n+1):
            res += dfs(str(num))
        return res