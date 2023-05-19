class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        res = ['999999999']
        def dfs(i, num):
            if i == len(pattern):
                res[0] = min(res[0], num)
                return
            if pattern[i] == 'I':
                last = num[-1]
                for j in range(int(last), 10):
                    if str(j) not in num:
                        dfs(i + 1, num + str(j))
            else:
                last = int(num[-1])
                for j in range(last - 1, 0, -1):
                    if str(j) not in num:
                        dfs(i + 1, num + str(j))
        dfs(0, '1'); dfs(0, '2'); dfs(0, '3'); dfs(0, '4'); dfs(0, '5')
        dfs(0, '6'); dfs(0, '7'); dfs(0, '8'); dfs(0, '9')
        return res[0]