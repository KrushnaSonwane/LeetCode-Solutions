class Solution(object):
    def maxScore(self, nums1, nums2, k):
        arr = [[n2, n1] for n2, n1 in zip(nums2, nums1)]
        arr.sort(reverse = True)
        queue, res, sum_ = [], 0, 0
        for i, (n2, n1) in enumerate(arr):
            sum_ += n1
            heapq.heappush(queue, n1)
            if k - 1 <= i:
                res = max(res, sum_ * n2)
                sum_ -= heapq.heappop(queue)
        return res