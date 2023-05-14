class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        if derived == [0]: return 1
        res = 0
        for num in derived:
            res ^= num
        return res == 0 and len(derived) > 1