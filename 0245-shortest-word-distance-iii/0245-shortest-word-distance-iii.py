class Solution:
    def shortestWordDistance(self, wordsDict: List[str], w1: str, w2: str) -> int:
        hashT = defaultdict(list)
        for i, w in enumerate(wordsDict):
            hashT[w].append(i)
        if w1 == w2:
            return min(hashT[w1][i]-hashT[w1][i-1] for i in range(1, len(hashT[w1])))
        res = inf
        for num in hashT[w1]:
            i = min(len(hashT[w2])-1, bisect_right(hashT[w2], num))
            res = min(res, abs(num-hashT[w2][i]))
            if i - 1 >= 0:
                res = min(res, abs(num-hashT[w2][i-1]))
        return res