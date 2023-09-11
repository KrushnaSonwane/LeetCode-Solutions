class Solution:
    def groupThePeople(self, GS: List[int]) -> List[List[int]]:
        GS = [[val, i] for i, val in enumerate(GS)]
        GS.sort()
        res, t = [], []
        for val, i in GS:
            t.append(i)
            if len(t)==val:
                res.append(t)
                t = []
        return res