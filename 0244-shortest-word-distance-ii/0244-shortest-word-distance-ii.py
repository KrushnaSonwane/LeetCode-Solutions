class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.hashT = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.hashT[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = inf
        for num in self.hashT[word1]:
            j = min(len(self.hashT[word2])-1, bisect_right(self.hashT[word2], num))
            res = min(res, abs(num-self.hashT[word2][j]))
            if j - 1 >= 0:
                res = min(res, abs(num-self.hashT[word2][j-1]))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)