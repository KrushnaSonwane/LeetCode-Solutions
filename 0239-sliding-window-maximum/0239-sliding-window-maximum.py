class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q, res = [], []
        for i, num in enumerate(nums):
            heappush(Q, [-num, i])
            while Q[0][1] <= i-k:
                heappop(Q)
            if i+1 >= k:
                res.append(-Q[0][0])
        return res