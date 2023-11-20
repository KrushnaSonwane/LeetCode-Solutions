class Solution:
    def garbageCollection(self, GBG: List[str], T: List[int]) -> int:
        res = 0
        for G in ["G", 'P', 'M']:
            count, dist = GBG[0].count(G), 0
            res += count
            for i in range(1, len(GBG)):
                dist += T[i-1]
                count = GBG[i].count(G)
                if count:
                    res += dist + count
                    dist, count = 0, 0
        return res