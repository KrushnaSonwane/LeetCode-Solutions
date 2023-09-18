class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        A, Q, res = Counter(s), [], [["", 0]]
        heapify(Q)
        for key in A:
            heappush(Q, [-ord(key), A[key]])
        while len(Q) > 1:
            a, aa = heappop(Q)
            b, bb = heappop(Q)
            if res[-1][0] != chr(-a):
                res.append([chr(-a), min(repeatLimit, aa)])
                res.append([chr(-b), 1])
                aa -= min(aa, repeatLimit)
                bb -= 1
                if aa > 0:
                    heappush(Q, [a, aa])
                if bb > 0:
                    heappush(Q, [b, bb])
            else:
                res.append([chr(-a), min(repeatLimit-res[-1][1], aa)])
                res.append([chr(-b), 1])
                aa -= min(repeatLimit-res[-1][1], aa)
                bb -= 1
                if aa > 0:
                    heappush(Q, [a, aa])
                if bb > 0:
                    heappush(Q, [b, bb])
        if Q:
            a, aa = heappop(Q)
            if res[-1][0] != chr(-a):
                res.append([chr(-a), min(repeatLimit, aa)])
            else:
                res.append([chr(-a), min(repeatLimit - res[-1][1], aa)])
        return ''.join(a * b for a, b in res)