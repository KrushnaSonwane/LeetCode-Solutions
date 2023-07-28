class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def dfs(num):
            if num==1: return 0
            if num%2: return min(dfs(num-1), dfs(num+1))+1
            return dfs(num//2)+1
        return dfs(n)