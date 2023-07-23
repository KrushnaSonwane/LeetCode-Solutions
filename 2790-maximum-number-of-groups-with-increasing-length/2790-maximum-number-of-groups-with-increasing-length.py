class Solution:
    def maxIncreasingGroups(self, A: List[int]) -> int:
        A.sort()
        n, sum_ = 1, 0
        for num in A:
            sum_ += num
            if sum_ >= (n * (n + 1)) // 2: n += 1
        return n-1