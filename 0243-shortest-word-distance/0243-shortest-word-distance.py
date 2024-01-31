class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        A, B = [], []
        for i, w in enumerate(wordsDict):
            if w == word1: A.append(i)
            elif w == word2: B.append(i)
        res = inf
        for num in A:
            j = min(len(B)-1, bisect_right(B, num))
            res = min(res, abs(num-B[j]))
            if j - 1 >= 0:
                res = min(res, abs(num-B[j-1]))
        return res