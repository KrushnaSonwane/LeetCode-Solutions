from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res, A = 0, SortedList()
        for num in nums[::-1]:
            res += bisect_right(A, num-1)
            A.add(num*2)
        return res