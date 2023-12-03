class Solution:
    def findPeaks(self, M: List[int]) -> List[int]:
        res = []
        for i in range(1, len(M)-1):
            if M[i-1] < M[i] > M[i+1]:
                res.append(i)
        return res