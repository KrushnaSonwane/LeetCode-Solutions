class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def getCount(i, j, c):
            res = 0
            while ring[i] != key[j]:
                if c: i += 1
                else: i -= 1
                if c and i == len(ring):
                    i = 0
                if not c and i == -1:
                    i = len(ring) - 1
                res += 1
            return i, res
            
        @cache
        def dfs(i, j):
            if j == len(key): return 0
            i1, a = getCount(i, j, 1)
            i2, b = getCount(i, j, 0)
            res = min(a + dfs(i1, j+1), b + dfs(i2, j+1)) + 1
            return res
        return dfs(0, 0)