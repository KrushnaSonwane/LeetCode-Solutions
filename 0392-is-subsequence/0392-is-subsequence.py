class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while len(s) > i and len(t) > j:
            if s[i]==t[j]:
                i +=1
            j += 1
        return i == len(s)