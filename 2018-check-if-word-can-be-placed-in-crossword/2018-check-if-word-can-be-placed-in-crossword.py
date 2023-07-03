class Solution:
    def placeWordInCrossword(self, A: List[List[str]], S: str) -> bool:
        m, n = len(A), len(A[0])
        def check(r, c, a):
            for k in range(len(a)):
                if A[r-k][c] == ' ': continue
                if a[len(a) - 1 - k] != A[r-k][c]: return 0
            return 1 

        def check2(r, c, a):
            for k in range(len(a)):
                if A[r][c-k] == ' ': continue
                if a[len(a)-1-k] != A[r][c-k]: return 0
            return 1
            
        for i in range(n):
            count = 0
            for j in range(m):
                if A[j][i] != '#': count += 1
                else: 
                    if count == len(S) and (check(j-1, i, S) or check(j-1,i,S[::-1])): return 1
                    count = 0
            if count == len(S) and (check(j, i, S) or check(j, i, S[::-1])): return 1
        
        for i in range(m):
            count = 0
            for j in range(n):
                if A[i][j] != '#': count += 1
                else:
                    if count == len(S) and (check2(i, j - 1, S) or check2(i,j-1,S[::-1])): return 1
                    count = 0
            if count == len(S) and (check2(i, j,S) or check2(i,j,S[::-1])): return 1
        return 0