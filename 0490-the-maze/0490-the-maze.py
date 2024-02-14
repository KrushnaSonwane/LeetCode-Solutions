class Solution:
    def hasPath(self, maze: List[List[int]], s: List[int], d: List[int]) -> bool:
        x, y = s
        Q, visit = [(x, y)], set({(x, y)})
        m, n = len(maze), len(maze[0])
        def check(a, b):
            if (a, b) not in visit:
                visit.add((a, b))
                Q.append((a, b))
        while Q:
            x, y = Q.pop(0)
            if [x, y] == d: return True
            a, b = x, y
            for j in range(y-1, -1, -1):
                if maze[a][j] == 1: break
                b = j
            check(a, b)
            a, b = x, y
            for j in range(b+1, n, 1):
                if maze[a][j] == 1: break
                b = j
            check(a, b)
            a, b = x, y
            for i in range(a+1, m, 1):
                if maze[i][b] == 1: break
                a = i
            check(a, b)
            a, b = x, y
            for i in range(a-1, -1, -1):
                if maze[i][b] == 1: break
                a = i
            check(a, b)
        return False