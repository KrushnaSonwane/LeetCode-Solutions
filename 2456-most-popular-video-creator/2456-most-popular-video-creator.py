class Solution:
    def mostPopularCreator(self, C: List[str], IDS: List[str], V: List[int]) -> List[List[str]]:
        hashT = {}
        max_ = 0
        for c, ids, v in zip(C, IDS, V): 
            if c not in hashT:
                hashT[c] = [0, []]
            hashT[c][0] += v
            hashT[c][1].append([v, ids])
            max_ = max(max_, hashT[c][0])
        res = []
        for c in hashT:
            if hashT[c][0] == max_:
                hashT[c][1].sort(key = lambda x: (-x[0], x[1]))
                res.append([c, hashT[c][1][0][1]])
        return res