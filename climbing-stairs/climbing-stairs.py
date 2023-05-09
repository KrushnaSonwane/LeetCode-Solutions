class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f, s = 1, 1
        for _ in range(n-1):
            curr = f + s
            f = s
            s = curr
        return s