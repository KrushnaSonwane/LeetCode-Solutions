class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res, visit = [], set({(0, 0)})
        n1, n2 = len(nums1), len(nums2)
        queue = [[nums1[0] + nums2[0], 0, 0]]
        heapq.heapify(queue)
        while k and queue:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            if i + 1 < n1 and (i + 1, j) not in visit:
                visit.add((i + 1, j))
                heapq.heappush(queue, [nums1[i + 1] + nums2[j], i + 1, j])
            if j + 1 < n2 and (i, j + 1) not in visit:
                visit.add((i, j + 1))
                heapq.heappush(queue, [nums1[i] + nums2[j + 1], i, j + 1])
            k -= 1
        return res