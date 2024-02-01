class Solution:
    def generatePossibleNextMoves(self, A: str) -> List[str]:
        res = []
        for i in range(1, len(A)):
            if A[i-1] == A[i] == '+':
                res.append(A[:i-1]+'--'+A[i+1:])
        return res