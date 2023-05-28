class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        visit = set()
        r, c = entrance
        visit.add((r, c))
        queue = [(r, c)]
        res = 0
        while queue:
            res += 1
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                for x, y in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
                    if (x, y) not in visit:
                        if x in [-1, m] or y in [-1, n] or maze[x][y] == '+': continue
                        if x in [0, m - 1] or y in [0, n - 1]: return res
                        queue.append((x, y))
                        visit.add((x, y))
        return -1