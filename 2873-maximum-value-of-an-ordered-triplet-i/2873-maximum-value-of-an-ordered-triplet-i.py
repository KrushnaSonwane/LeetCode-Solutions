class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_ = nums[0]
        Q = []
        heapify(Q)
        for i, num in enumerate(nums):
            heappush(Q, [-num, i])
        res = 0
        for i in range(1, len(nums)):
            while Q and Q[0][1] <= i:
                heappop(Q)
            if Q:
                res = max(res, (max_ - nums[i]) * (-Q[0][0]))
            max_ = max(max_, nums[i])
        return res