class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        visit, m, n = set(), len(mat), len(mat[0])
        Q = [[0, ''.join(str(li) for AA in mat for li in AA)]]
        while Q:
            cost, A = heappop(Q)
            if sum(int(li) for li in A) == 0: return cost
            for i in range(m):
                for j in range(n):
                    a = 0
                    B = []
                    for b in range(m):
                        t = []
                        for c in range(n):
                            t.append(int(A[a]))
                            a += 1
                        B.append(t)
                    for x, y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                        if x in [-1, m] or y in [-1, n]: continue
                        B[x][y] = int(not B[x][y])
                    B[i][j] = int(not B[i][j])
                    temp = ''
                    for li in B:
                        for ll in li:
                            temp += str(ll)
                    if temp not in visit:
                        heappush(Q, [cost+1, temp])
                        visit.add(temp)
        return -1