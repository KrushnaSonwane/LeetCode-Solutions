class Solution:
    def slidingPuzzle(self, A: List[List[int]]) -> int:
        currPos = ''
        for i in range(2):
            for j in range(3):
                if not A[i][j]: r, c = i, j
                currPos += str(A[i][j])
        visit = set({currPos})
        res = 0
        Q = [[currPos, r, c]]
        while Q:
            for _ in range(len(Q)):
                curr, x, y = Q.pop(0)
                if curr == '123450': return res
                B = []
                t1, t2 = [], []
                for i in range(3):
                    t1.append(int(curr[i]))
                    t2.append(int(curr[i+3]))
                B.append(t1)
                B.append(t2)
                for xx, yy in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                    if xx in [-1, 2] or yy in [-1, 3]: continue
                    B[x][y], B[xx][yy] = B[xx][yy], B[x][y]
                    currPos = ''
                    for i in range(2):
                        for j in range(3):
                            currPos += str(B[i][j])
                    if currPos not in visit:
                        visit.add(currPos)
                        Q.append([currPos, xx, yy])
                    B[x][y], B[xx][yy] = B[xx][yy], B[x][y]
            res += 1
        return -1