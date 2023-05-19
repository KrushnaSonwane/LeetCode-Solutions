class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        score = [0] * len(edges)
        for i, node in enumerate(edges):
            score[node] += i
        max_ = max(score)
        for i, val in enumerate(score):
            if val == max_: return i
        return -1