class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        hashT = defaultdict(list)
        for a, b in edges:
            hashT[b].append(a)
        return [i for i in range(n) if not hashT[i]]