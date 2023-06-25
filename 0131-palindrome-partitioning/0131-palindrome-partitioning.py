class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isValid(arr):
            for ch in arr: 
                if ch != ch[::-1]: return 0
            return 1
        def dfs(i, ans):
            if i == len(s):
                if isValid(ans): res.append(ans)
                return
            for j in range(i, len(s)):
                dfs(j + 1, ans + [s[i: j+1]])
        dfs(0, [])
        return res