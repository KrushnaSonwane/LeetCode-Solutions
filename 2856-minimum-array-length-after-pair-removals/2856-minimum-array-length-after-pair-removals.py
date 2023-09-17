class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        A = Counter(nums)
        Q = []
        heapify(Q)
        for num in A.values():
            heappush(Q, -num)
        res = 0
        while len(Q) > 1:
            a, b = -heappop(Q), -heappop(Q)
            res += 2
            if a - 1 > 0:
                heappush(Q, -(a-1))
            if b - 1 > 0:
                heappush(Q, -(b-1))
        return len(nums) - res