class Solution:
    def fullBloomFlowers(self, A: List[List[int]], P: List[int]) -> List[int]:
        A.sort()
        P = sorted([val, i] for i, val in enumerate(P))
        Q, res, i = [], [0 for _ in P], 0
        heapify(Q)
        for key, j in P:
            while i < len(A) and A[i][0] <= key:
                heappush(Q, A[i][1])
                i += 1
            while Q and Q[0] < key:
                heappop(Q)
            res[j] = len(Q)
        return res