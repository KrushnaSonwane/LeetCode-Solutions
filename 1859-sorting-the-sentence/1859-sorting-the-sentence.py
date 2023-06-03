class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        res = []
        for val in arr:
            res.append([val[-1], val[:-1]])
        res.sort()
        return ' '.join(val for _, val in res)