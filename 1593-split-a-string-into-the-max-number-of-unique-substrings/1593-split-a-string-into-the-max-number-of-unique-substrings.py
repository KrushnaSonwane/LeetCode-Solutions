class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, res):
            if i == len(s):
                return 0
            ans = 0
            for j in range(i, len(s)):
                if s[i:j + 1] not in res:
                    res.add(s[i: j + 1])
                    ans = max(ans, dfs(j + 1, res) + 1)
                    res.discard(s[i:j+1])
            return ans
        return dfs(0, set())