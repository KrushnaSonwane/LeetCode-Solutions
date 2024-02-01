class Solution:
    def canAttendMeetings(self, A: List[List[int]]) -> bool:
        A.sort()
        for i in range(1, len(A)):
            if A[i][0] >= A[i-1][1]: continue
            return False
        return True