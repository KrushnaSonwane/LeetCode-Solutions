class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        if s[0] == '0': return -1
        visit = set()
        for i in range(20):
            visit.add(pow(5, i))
        def getDecimal(temp):
            num = 0
            c = 0
            for t in temp[::-1]:
                if t == '1':
                    num = (pow(2, c) + num)
                c += 1
            return num
        
        def dfs(i):
            if i == len(s): return 0
            res = float("inf")
            for j in range(i, len(s)):
                if j + 1 < len(s) and s[j+1] == '0': continue
                if getDecimal(s[i: j+1]) in visit:
                    res = min(res, dfs(j+1) + 1)
            return res
        res = dfs(0)
        
        return -1 if res == float("inf") else res