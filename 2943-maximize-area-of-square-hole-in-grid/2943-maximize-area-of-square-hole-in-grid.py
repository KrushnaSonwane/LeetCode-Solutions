class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, h: List[int], v: List[int]) -> int:
        v.sort()
        h.sort()
        vG, hG = 0, 0
        last = 1
        count = 1
        for num in h:
            if num == last + 1:
                count += 1
                last += 1
            else:
                count = 2
                last = num
            hG = max(hG, count)
        last = 1
        count=1
        for num in v:
            if num == last + 1:
                count += 1
            else:
                count = 2
            vG = max(vG, count)
            last = num
        return min(vG, hG) * min(vG, hG)