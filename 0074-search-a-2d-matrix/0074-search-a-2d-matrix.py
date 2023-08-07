class Solution:
    def searchMatrix(self, A: List[List[int]], key: int) -> bool:
        m, n = len(A), len(A[0])
        l, r = 0, m*n-1
        while r >= l:
            mid = (r+l)//2
            i, j = mid//n, mid%n
            if A[i][j]==key: 
                return True
            elif A[i][j] > key:
                r = mid - 1
            else:
                l = mid + 1
        return False