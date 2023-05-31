class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = float("inf")
        for num in range(1, 7):
            swap = 0
            for i, val in enumerate(tops):
                if val == num: continue
                if bottoms[i] == num:
                    swap += 1
                else: break
            else:
                res = min(res, swap)
            swap = 0
            for i, val in enumerate(bottoms):
                if val == num: continue
                if tops[i] == num:
                    swap += 1
                else: break
            else:
                res = min(res, swap)
        return res if res != float("inf") else -1