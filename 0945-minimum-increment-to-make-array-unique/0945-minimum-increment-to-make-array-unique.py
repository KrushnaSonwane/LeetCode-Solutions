class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        A.sort()
        visit, curr, res = set(), 0, 0
        for a in A:
            while curr < a or curr in visit: curr += 1
            visit.add(curr)
            res += curr - a
        return res