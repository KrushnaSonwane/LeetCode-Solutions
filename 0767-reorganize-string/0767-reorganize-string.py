class Solution:
    def reorganizeString(self, s: str) -> str:
        hashT, res = Counter(s), ['']*len(s)
        A = sorted([[hashT[ch], ch] for ch in hashT])[::-1]
        if ceil(len(s)/2) < A[0][0]: return ''
        i = 0
        for count, ch in A:
            for _ in range(count):
                res[i] = ch
                i += 2
                if i >= len(s):
                    i = 1
        return ''.join(res)