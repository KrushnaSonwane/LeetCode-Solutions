class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp, n = [0]*len(s), len(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == '(': stack.append(ch)
            else:
                if not stack: continue
                else:
                    dp[i] = 2 + dp[i - 1]
                    if i - dp[i] >= 0:
                        dp[i] += dp[i - dp[i]]
                    stack.pop()
        return max(dp)