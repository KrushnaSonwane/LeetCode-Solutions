class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(open, close, s):
            if not open:
                s += ')' * close
                res.append(s)
                return
            if open == close:
                dfs(open - 1, close, s + '(')
            else:
                dfs(open - 1, close, s + '(')
                dfs(open, close - 1, s + ')')
        res = []
        dfs(n, n, '')
        return res