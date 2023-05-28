class Solution:
    def halveArray(self, nums: List[int]) -> int:
        queue = []
        for num in nums:
            heapq.heappush(queue, -num)
        sum_, curr, res = sum(nums), 0, 0
        while sum_ - curr > sum_ / 2:
            ele = -heappop(queue)
            curr += ele / 2
            heappush(queue, -ele / 2)
            res += 1
        return res