from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], diff: int) -> int:
        nums, res = SortedList(), 0
        for a, b in zip(A, B):
            curr = -b + a + diff
            res += bisect_right(nums, curr)
            nums.add(a - b)
        return res