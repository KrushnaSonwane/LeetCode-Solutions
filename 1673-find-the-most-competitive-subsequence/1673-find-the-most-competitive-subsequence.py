from sortedcontainers import SortedList
class Solution:
    def mostCompetitive(self, A: List[int], k: int) -> List[int]:
        res = []
        for i, num in enumerate(A):
            while res and k - len(res) < len(A)-i and res[-1] > num:
                res.pop()
            if len(res) < k:
                res.append(num)
        return res