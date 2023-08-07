class Solution:
    def searchMatrix(self, A: List[List[int]], key: int) -> bool:
        m, n = len(A), len(A[0])
        i, j = 0, n-1
        while m > i and -1 < j:
            if A[i][j]==key: return True
            if i+1<m and A[i+1][j] <= key:
                i+=1
            else:
                j-=1
        return False