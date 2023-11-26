from sortedcontainers import SortedList
class Solution:
    def lexicographicallySmallestArray(self, BB: List[int], limit: int) -> List[int]:
        nums = [[BB[i], i] for i in range(len(BB))]
        nums.sort()
        res = [-1 for _ in nums]
        A = SortedList()
        A.add(nums[0][1])
        j = 0
        for i in range(1, len(nums)):
            if abs(nums[i-1][0] - nums[i][0]) <= limit:
                A.add(nums[i][1])
            else:
                k = 0
                while k < len(A):
                    res[A[k]] = nums[j][0]
                    j += 1
                    k += 1
                A = SortedList()
                A.add(nums[i][1])
        k = 0
        while k < len(A):
            res[A[k]] = nums[j][0]
            j += 1
            k += 1
        return res