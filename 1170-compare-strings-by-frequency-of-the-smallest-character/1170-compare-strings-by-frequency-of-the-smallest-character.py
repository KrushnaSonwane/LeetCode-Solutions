class Solution:
    def numSmallerByFrequency(self, Q: List[str], W: List[str]) -> List[int]:
        A, n, res = [], len(W), []
        for word in W:
            T = collections.Counter(word)
            A.append(T[min(T.keys())])
        A.sort()
        for q in Q:
            T = collections.Counter(q)
            ind = bisect.bisect_left(A, T[min(T.keys())]+1)
            res.append(n - ind)
        return res