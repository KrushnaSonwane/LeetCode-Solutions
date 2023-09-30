class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        A = set()
        res = 0
        for num in nums[::-1]:
            res += 1
            if num <= k:
                A.add(num)
            if len(A) == k: return res
        return -1