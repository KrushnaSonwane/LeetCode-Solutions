class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def dfs(size):
            visit = set()
            for i in range(size):
                visit.add((cells[i][0] - 1, cells[i][1] - 1))
            Q = []
            for i in range(col):
                if (0, i) not in visit: Q.append((0, i))
            while Q:
                i, j = Q.pop(0)
                if i == row - 1: return 1
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if x in [-1, row] or y in [-1, col] or (x, y) in visit: continue
                    Q.append((x, y))
                    visit.add((x,y))
            return False
        l, r = 0, len(cells)
        while r > l:
            mid = (r + l) // 2
            if dfs(mid): l = mid + 1
            else: r = mid
        return l - 1