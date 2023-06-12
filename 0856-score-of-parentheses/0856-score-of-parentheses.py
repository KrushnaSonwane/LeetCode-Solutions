class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def dfs(l, r):
            res = count = 0
            for i in range(l, r + 1):
                count += 1 if s[i] == '(' else -1
                if count == 0:
                    res += 1 if i - l == 1 else 2 * dfs(l + 1, i - 1)
                    l = i + 1
            return res
        return dfs(0, len(s) - 1)