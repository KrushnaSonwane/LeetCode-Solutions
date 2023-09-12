class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        A = sorted([[len(W), W] for W in words])[::-1]
        hashT, count, res = set(), 0, 0
        for _, W in A:
            if W not in hashT:
                count += 1
                res += len(W)
            for i in range(len(W)):
                hashT.add(W[i:])
        return res + count