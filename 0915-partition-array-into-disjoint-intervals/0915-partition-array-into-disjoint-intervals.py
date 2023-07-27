class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        Q, max_ = [], -inf
        for i, num in enumerate(nums):
            heappush(Q, [num, i])
        for i in range(len(nums)):
            max_ = max(max_, nums[i])
            while Q[0][1] <= i:
                heappop(Q)
            if Q[0][0] >= max_: return i+1
        return -1