class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        res, A = 0, defaultdict(int)
        for w, h in rectangles:
            curr = w / h
            res += A[curr]
            A[curr] += 1
        return res