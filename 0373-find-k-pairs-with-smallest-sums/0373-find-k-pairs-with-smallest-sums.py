class Solution(object):
    def kSmallestPairs(self, n1, n2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n, res, A = len(n1), len(n2), [], [[n1[0] + n2[0], 0,0]]
        visit = {(0, 0)}
        while A and k:
            _, i, j = heappop(A)
            res.append([n1[i], n2[j]])
            for x, y in [[i + 1, j], [i, j + 1]]:
                if x < m and y < n and (x, y) not in visit:
                    visit.add((x, y))
                    heappush(A, [n1[x]+n2[y], x, y])
            k -= 1
        return res