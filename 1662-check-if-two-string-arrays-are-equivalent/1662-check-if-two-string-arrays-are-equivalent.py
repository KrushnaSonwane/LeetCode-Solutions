class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1 = ''
        str2 = ''
        for i in word1:
            str1 += i
        for i in word2:
            str2 += i
        if str1 == str2:
            return True
        else:
            return False