class Solution:
    def rotatedDigits(self, n: int) -> int:
        def dfs(s):
            for d in ['3', '4', '7']:
                if d in s: return 0
            for d in ['2', '5', '6', '9']:
                if d in s: return 1
            return 0
        return sum(dfs(str(i)) for i in range(1, n+1))