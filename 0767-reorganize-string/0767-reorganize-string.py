class Solution:
    def reorganizeString(self, s: str) -> str:
        hashT, res = Counter(s), [""]
        Q = []
        for ch in hashT: heappush(Q, [-hashT[ch], ch])
        while len(Q)>1:
            a, c1 = heappop(Q)
            b, c2 = heappop(Q)
            if res[-1]==c1:
                c1, c2 = c2, c1
                a, b = b, a
            res.append(c1)
            res.append(c2)
            if a+1 < 0: heappush(Q, [a+1, c1])
            if b+1 < 0: heappush(Q, [b+1, c2])
        if Q:
            a, c = heappop(Q)
            if a != -1: return ''
            res.append(c)
        return ''.join(res)