class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        visit, res, curr = set(), 0, 1
        while len(visit) != n:
            if k - curr not in visit:
                visit.add(curr)
            curr += 1
        return sum(visit)