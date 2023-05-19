class Solution(object):
    def wordCount(self, startWords, targetWords):
        """
        :type startWords: List[str]
        :type targetWords: List[str]
        :rtype: int
        """
        hashT, res = set(), 0
        for word in startWords:
            hashT.add(''.join(sorted(word)))
        for word in targetWords:
            curr = sorted(word)
            for i, ch in enumerate(curr):
                flag = False
                currWord = ''
                for j, ch2 in enumerate(curr):
                    if i == j: continue
                    currWord += ch2
                if currWord in hashT:
                    res += 1
                    flag = True
                    break
        return res