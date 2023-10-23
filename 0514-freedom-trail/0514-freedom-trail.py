class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def dfs(i, j):
            print(i, j)
            if j == len(key): return 0
            a, p1 = 0, i
            while ring[p1] != key[j]:
                p1 += 1
                a += 1
                if p1 == len(ring):
                    p1 = 0
            b, p2 = 0, i
            while ring[p2] != key[j]:
                p2 -= 1
                b += 1
                if p2 == -1:
                    p2 = len(ring) - 1
            res = min(a + dfs(p1, j+1), b + dfs(p2, j+1)) + 1
            return res
        return dfs(0, 0)