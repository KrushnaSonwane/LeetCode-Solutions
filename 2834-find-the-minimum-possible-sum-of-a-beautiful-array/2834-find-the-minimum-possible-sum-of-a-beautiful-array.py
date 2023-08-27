class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        visit = set()
        res, num = 0, 1
        for _ in range(n):
            while target - num in visit:
                num += 1
            res += num
            visit.add(num)
            num += 1
        return res