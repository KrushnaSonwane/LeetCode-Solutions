class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for A in matrix:
            l, r = 0, len(A)-1
            while r >= l:
                mid = (r+l)//2
                if A[mid]>target:
                    r = mid - 1
                elif A[mid]<target:
                    l = mid + 1
                else: return True
        return False