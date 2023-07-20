class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row, col = defaultdict(list), defaultdict(list)
        for a, b in stones:
            row[a].append((a, b))
            col[b].append((a, b))
        res, visit = 0, set()
        
        def dfs2(t):
            curr = 0
            for r, c in col[t]:
                if (r, c) not in visit:
                    visit.add((r, c))
                    curr = dfs1(r) + dfs2(c) + 1
            return curr

        def dfs1(t):
            curr = 0
            for r, c in row[t]:
                if (r, c) not in visit:
                    visit.add((r, c))
                    curr = dfs1(r) + 1 + dfs2(c)
            return curr

        for a, b in stones:
            if (a, b) not in visit:
                visit.add((a, b))
                res += dfs1(a) + dfs2(b)
        return res