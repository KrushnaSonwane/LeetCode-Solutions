class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        visit, num = set(), 1
        for _ in range(n):
            while target - num in visit:
                num += 1
            visit.add(num)
            num += 1
        return sum(visit)