class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = 0
        for i in t:
            if a == len(s):
                return True
            if s[a] == i:
                a += 1
        else:
            if len(s) == a:
                return True
            else:
                return False