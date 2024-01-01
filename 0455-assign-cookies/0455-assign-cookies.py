class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i, j, res = 0, 0, 0
        g.sort()
        s.sort()
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j < len(s) and s[j] >= g[i]:
                res += 1
                j += 1
            i += 1
        return res