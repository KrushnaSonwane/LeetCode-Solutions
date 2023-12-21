class Solution:
    def maxWidthOfVerticalArea(self, A: List[List[int]]) -> int:
        A.sort()
        return max(A[i][0]-A[i-1][0] for i in range(1, len(A)))