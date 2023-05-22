class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashT = collections.Counter(nums)
        queue = [[-hashT[val], val] for val in hashT]
        heapq.heapify(queue)
        return [heapq.heappop(queue)[1] for _ in range(min(k, len(queue)))]