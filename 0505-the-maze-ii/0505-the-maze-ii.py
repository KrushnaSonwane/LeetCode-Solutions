class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], d: List[int]) -> int:
        dist = {}
        x, y = start
        m, n = len(maze), len(maze[0])
        Q = [(0, x, y)]
        dist[(x, y)] = 0
        def check(a, b, c):
            if (a, b) in dist and dist[(a, b)] <= c: return
            Q.append((c, a, b))
            dist[(a, b)] = c
        while Q:
            cost, x, y = heappop(Q)
            a, b, c = x, y, cost
            for j in range(b-1, -1, -1):
                if maze[a][j] == 1: break
                c += 1
                b = j
            check(a, b, c)
            a, b, c = x, y, cost
            for j in range(b+1, n, 1):
                if maze[a][j] == 1: break
                c += 1
                b = j
            check(a, b, c)
            a, b, c = x, y, cost
            for i in range(a-1, -1, -1):
                if maze[i][b] == 1: break
                c += 1
                a = i
            check(a, b, c)
            a, b, c = x, y, cost
            for i in range(a+1, m, 1):
                if maze[i][b] == 1: break
                c += 1
                a = i
            check(a, b, c)
        a, b = d
        if (a, b) in dist: return dist[(a, b)]
        return -1