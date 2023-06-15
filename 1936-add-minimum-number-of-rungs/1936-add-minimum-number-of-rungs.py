class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        res = last = 0
        for num in rungs:
            diff = num - last - 1
            res += diff // dist
            last = num
        return res