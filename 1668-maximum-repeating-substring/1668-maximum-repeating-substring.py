class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        ans = 1
        while word * ans in sequence:
            ans += 1
        return ans - 1