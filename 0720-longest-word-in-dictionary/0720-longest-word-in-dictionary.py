class Solution:
    def longestWord(self, words: List[str]) -> str:
        A = [[len(W), W] for W in words]
        A.sort()
        res, visit = '', set({""})
        for _, W in A:
            if W[:-1] in visit:
                visit.add(W)
                if _ > len(res): res = W
                elif _ == len(res): res = min(res, W)
        return res