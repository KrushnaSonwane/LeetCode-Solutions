class Solution:
    def maximumBeauty(self, B: List[List[int]], Q: List[int]) -> List[int]:
        A = [[val, i] for i, val in enumerate(Q)]
        A.sort()
        B.sort()
        max_, res, j = 0, [0]*len(A), 0
        for val, i in A:
            while len(B) > j and B[j][0] <= val:
                max_ = max(B[j][1], max_)
                j += 1
            res[i] = max_
        return res