class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, res = n, 0
        while num != 1:
            res += num // 2
            num = (num // 2) + (num % 2)
        return res