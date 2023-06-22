class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        hashT = {}
        for i, number in enumerate(strs):
            hashT[i] = [0, 0]
            for ch in number:
                if ch == '0': hashT[i][0] += 1
                else: hashT[i][1] += 1

        dp = {}
        def dfs(i, x, y):
            if (i, x, y) not in dp:
                if i == len(strs): return 0
                res = dfs(i + 1, x, y)
                t1, t2 = x, y
                x -= hashT[i][0]
                y -= hashT[i][1]
                if x >= 0 and y >= 0:
                    res = max(res, dfs(i + 1, x, y) + 1)
                x, y = t1, t2
                dp[(i, x, y)] = res
            return dp[(i, x, y)]
        return dfs(0, m, n)