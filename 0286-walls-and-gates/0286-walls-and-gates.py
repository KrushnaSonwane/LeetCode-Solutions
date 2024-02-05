class Solution:
    def wallsAndGates(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visit, Q = set(), []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == -1:
                    visit.add((i, j))
                elif A[i][j] == 0:
                    Q.append((i, j, 1))
                    visit.add((i, j))
        while Q:
            for _ in range(len(Q)):
                i, j, count = Q.pop(0)
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (x, y) not in visit and 0 <= x < len(A) and 0 <= y < len(A[0]):
                        A[x][y] = count
                        Q.append((x, y, count+1))
                        visit.add((x, y))