from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, A: List[int], B: List[int], diff: int) -> int:
        nums, res = SortedList(), 0
        for a, b in zip(A, B):
            curr = -b + a + diff
            l, r = 0, len(nums)-1
            res += bisect_right(nums, curr)
            nums.add(a - b)
        return res