class Solution(object):
    def ladderLength(self, bW, eW, WL):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        hashT = {word: 0 for word in WL}
        hashT[bW] = 1
        allCh = "abcdefghijklmnopqrstuvwxyz"
        res, queue = 1, [bW]
        while queue:
            for _ in range(len(queue)):
                currWord = list(queue.pop(0))
                if currWord == list(eW): return res
                for i in range(len(currWord)):
                    for ch in allCh:
                        back = currWord[i]
                        currWord[i] = ch
                        temp = ''.join(currWord)
                        if temp in hashT and not hashT[temp]:
                            queue.append(temp)
                            hashT[temp] = 1
                        currWord[i] = back
            res += 1
        return 0