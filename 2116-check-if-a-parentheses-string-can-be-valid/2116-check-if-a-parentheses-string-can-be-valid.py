class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 == 1: return False
        rem = 0
        for i, ch in enumerate(s):
            rem += 1 if ch == '(' or locked[i] == '0' else -1
            if 0 > rem: return False
        rem = 0
        for i in range(n - 1, -1, -1):
            rem += 1 if s[i] == ')' or locked[i] == '0' else -1
            if 0 > rem: return False
        return True