class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return p1 == m