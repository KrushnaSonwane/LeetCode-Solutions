class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = [[num, c] for num, c in zip(nums, cost)]
        arr.sort()
        mid = sum(cost) // 2 + 1
        res = sum_ = 0
        for _, c in arr:
            sum_ += c
            if sum_ >= mid:
                mid = _
                break
        return sum(abs(num - mid) * c for num, c in arr)