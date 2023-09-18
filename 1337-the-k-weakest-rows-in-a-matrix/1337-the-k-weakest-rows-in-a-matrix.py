class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        Q = []
        for i, row in enumerate(mat):
            heappush(Q, [row.count(1), i])
        return [heappop(Q)[1] for _ in range(k)]