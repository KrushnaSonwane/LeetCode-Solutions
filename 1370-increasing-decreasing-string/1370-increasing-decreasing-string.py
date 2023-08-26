class Solution:
    def sortString(self, s: str) -> str:
        hashT = Counter(s)
        res, Q = [], []
        for ch in hashT:
            heappush(Q, [ord(ch), hashT[ch]])
        f = True
        while Q:
            t = []
            for _ in range(len(Q)):
                ch, count = heappop(Q)
                res.append(chr(abs(ch)))
                count -= 1
                if count != 0: heappush(t, [-ch if f else abs(ch), count])
            Q = t
            f = not f
        return ''.join(res)