class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        curr = target
        res = 0
        while curr != 1:
            if not maxDoubles:
                res += curr - 1
                curr = 1
            else:
                if not curr % 2 and maxDoubles:
                    curr //= 2
                    maxDoubles -= 1
                else:
                    curr -= 1
                res += 1
        return res