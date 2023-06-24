class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashT = collections.Counter(words)
        res = 0
        res2 = 0
        for ch in hashT:
            if ch == ch[::-1]:
                res2 += hashT[ch] // 2
            else:
                if ch[::-1] in hashT:
                    res += min(hashT[ch], hashT[ch[::-1]])
        return res // 2 + res2