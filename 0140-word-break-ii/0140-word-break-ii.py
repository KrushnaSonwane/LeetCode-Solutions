class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res, ans = [], []
        def dfs(i):
            if i == len(s):
                res.append(''.join(ans.copy())[1:])
                return
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)]==w:
                    ans.append(' '+w)
                    dfs(i+len(w))
                    ans.pop()
        dfs(0)
        return res